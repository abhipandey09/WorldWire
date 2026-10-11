import os
import time
import hashlib
import secrets
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import logging

load_dotenv()

def get_db_url():
    url = os.getenv("WORLDWIRE_DATABASE_URL") or os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("DATABASE_URL or WORLDWIRE_DATABASE_URL environment variable is not set. Please specify it in .env or Secret Manager")
    if "channel_binding=require" in url:
        url = url.replace("&channel_binding=require", "").replace("?channel_binding=require", "?")
    return url


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WorldWire.DB")

def hash_password(password: str) -> str:
    """Generate a secure salted PBKDF2 hash for admin authentication."""
    salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()
    return f"{salt}:{h}"

def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a plain password against the stored salted PBKDF2 hash."""
    try:
        salt, h = stored_hash.split(":")
        check = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()
        return h == check
    except Exception:
        return False

def get_connection(retries: int = 4, delay: float = 2.0):
    """Get a connection to Neon PostgreSQL with automatic retries for serverless cold-starts."""
    last_err = None
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(get_db_url(), connect_timeout=15)
            return conn
        except Exception as e:
            last_err = e
            logger.warning(f"Connection attempt {attempt+1}/{retries} failed: {e}. Retrying in {delay}s...")
            time.sleep(delay)
            delay *= 1.5
    raise last_err

def execute_with_retry(fn):
    """Decorator or helper to execute db operations with reconnection."""
    def wrapper(*args, **kwargs):
        retries = 3
        delay = 1.5
        for attempt in range(retries):
            try:
                return fn(*args, **kwargs)
            except (psycopg2.OperationalError, psycopg2.InterfaceError) as e:
                logger.warning(f"DB operation attempt {attempt+1} failed: {e}. Retrying...")
                if attempt == retries - 1:
                    raise
                time.sleep(delay)
    return wrapper

@execute_with_retry
def init_db():
    """Initialize database tables, admin users, and schema migrations."""
    query = """
    CREATE TABLE IF NOT EXISTS news_articles (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        summary TEXT NOT NULL,
        content TEXT NOT NULL,
        category VARCHAR(100) DEFAULT 'World',
        hot_topic_tag VARCHAR(100) DEFAULT 'Trending',
        image_url TEXT,
        source_name VARCHAR(255) DEFAULT 'WorldWire Intel',
        source_url TEXT,
        region VARCHAR(100) DEFAULT 'Global',
        published_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

    ALTER TABLE news_articles ADD COLUMN IF NOT EXISTS status VARCHAR(50) DEFAULT 'published';
    ALTER TABLE news_articles ADD COLUMN IF NOT EXISTS author VARCHAR(255) DEFAULT 'Abhishek Pandey, WorldWire Desk';

    CREATE INDEX IF NOT EXISTS idx_news_published_at ON news_articles (published_at DESC);
    CREATE INDEX IF NOT EXISTS idx_news_category ON news_articles (category);
    CREATE INDEX IF NOT EXISTS idx_news_status ON news_articles (status);
    CREATE UNIQUE INDEX IF NOT EXISTS idx_news_title ON news_articles (title);

    CREATE TABLE IF NOT EXISTS admin_users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role VARCHAR(50) DEFAULT 'admin',
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            # Ensure existing articles have status = 'published'
            cur.execute("UPDATE news_articles SET status = 'published' WHERE status IS NULL;")
            cur.execute("UPDATE news_articles SET author = 'Abhishek Pandey, WorldWire Desk' WHERE author IS NULL;")
            
            # Ensure admin user 'abhishek' exists
            cur.execute("SELECT id FROM admin_users WHERE username = 'abhishek';")
            if not cur.fetchone():
                admin_pw_hash = hash_password("Admin@1998")
                cur.execute(
                    "INSERT INTO admin_users (username, password_hash, role) VALUES (%s, %s, %s);",
                    ('abhishek', admin_pw_hash, 'admin')
                )
                logger.info("Admin user 'abhishek' initialized successfully.")

        conn.commit()
        logger.info("Database and admin authentication initialized successfully.")
    finally:
        conn.close()

@execute_with_retry
def verify_admin_credentials(username: str, password: str) -> bool:
    """Authenticate admin user against database records."""
    if not username or not password:
        return False
    query = "SELECT password_hash FROM admin_users WHERE LOWER(username) = LOWER(%s);"
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, (username.strip(),))
            row = cur.fetchone()
            if row:
                return verify_password(password, row[0])
            return False
    finally:
        conn.close()

@execute_with_retry
def insert_article(article_data: dict, default_status: str = "in_review") -> bool:
    """Insert a new article into the database with default status."""
    data = dict(article_data)
    if "status" not in data or not data["status"]:
        data["status"] = default_status
    if "author" not in data or not data["author"]:
        data["author"] = "Abhishek Pandey, WorldWire Desk"

    query = """
    INSERT INTO news_articles (
        title, summary, content, category, hot_topic_tag, 
        image_url, source_name, source_url, region, published_at, status, author
    ) VALUES (
        %(title)s, %(summary)s, %(content)s, %(category)s, %(hot_topic_tag)s,
        %(image_url)s, %(source_name)s, %(source_url)s, %(region)s, %(published_at)s,
        %(status)s, %(author)s
    )
    ON CONFLICT (title) DO NOTHING
    RETURNING id;
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, data)
            row = cur.fetchone()
            conn.commit()
            return row is not None
    finally:
        conn.close()

@execute_with_retry
def get_articles(limit: int = 50, category: str = None, search: str = None, status: str = "published"):
    """Retrieve articles ordered by latest published_at."""
    conditions = []
    params = {}
    
    if status and status.lower() != 'all':
        conditions.append("status = %(status)s")
        params['status'] = status

    if category and category.lower() != 'all':
        conditions.append("LOWER(category) = LOWER(%(category)s)")
        params['category'] = category

    if search:
        conditions.append("(title ILIKE %(search)s OR summary ILIKE %(search)s OR content ILIKE %(search)s)")
        params['search'] = f"%{search}%"

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    params['limit'] = limit

    query = f"""
    SELECT id, title, summary, content, category, hot_topic_tag,
           image_url, source_name, source_url, region, published_at, created_at, status, author
    FROM news_articles
    {where_clause}
    ORDER BY published_at DESC, id DESC
    LIMIT %(limit)s;
    """

    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchall()
    finally:
        conn.close()

@execute_with_retry
def get_article_by_id(article_id: int):
    """Retrieve a single article by its primary key ID."""
    if not article_id:
        return None
    query = """
    SELECT id, title, summary, content, category, hot_topic_tag,
           image_url, source_name, source_url, region, published_at, created_at, status, author
    FROM news_articles
    WHERE id = %s
    LIMIT 1;
    """
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, (article_id,))
            return cur.fetchone()
    finally:
        conn.close()

@execute_with_retry
def get_pending_articles(limit: int = 50):
    """Retrieve articles waiting for admin review and approval."""
    return get_articles(limit=limit, status="in_review")

@execute_with_retry
def update_article_status(article_id: int, status: str) -> bool:
    """Update status of an article (e.g. 'published', 'rejected', 'in_review')."""
    query = """
    UPDATE news_articles 
    SET status = %s, published_at = NOW() 
    WHERE id = %s;
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, (status, article_id))
            conn.commit()
            return cur.rowcount > 0
    finally:
        conn.close()

@execute_with_retry
def update_article(article_id: int, update_data: dict) -> bool:
    """Update article content fields."""
    allowed = ["title", "summary", "content", "category", "region", "source_name", "source_url", "image_url", "status", "author"]
    fields = []
    values = []
    for k, v in update_data.items():
        if k in allowed:
            fields.append(f"{k} = %s")
            values.append(v)
    
    if not fields:
        return False
        
    values.append(article_id)
    query = f"UPDATE news_articles SET {', '.join(fields)} WHERE id = %s;"
    
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, tuple(values))
            conn.commit()
            return cur.rowcount > 0
    finally:
        conn.close()

@execute_with_retry
def delete_article(article_id: int) -> bool:
    """Permanently delete an article from the database."""
    query = "DELETE FROM news_articles WHERE id = %s;"
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, (article_id,))
            conn.commit()
            return cur.rowcount > 0
    finally:
        conn.close()

@execute_with_retry
def get_latest_article():
    """Retrieve the single most recent published article."""
    query = """
    SELECT * FROM news_articles
    WHERE status = 'published'
    ORDER BY published_at DESC, id DESC
    LIMIT 1;
    """
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchone()
    finally:
        conn.close()

@execute_with_retry
def get_stats():
    """Retrieve database statistics."""
    query = """
    SELECT 
        COUNT(*) as total_articles,
        COUNT(CASE WHEN status = 'published' THEN 1 END) as published_count,
        COUNT(CASE WHEN status = 'in_review' THEN 1 END) as in_review_count,
        MAX(published_at) as last_updated,
        COUNT(DISTINCT category) as category_count
    FROM news_articles;
    """
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchone()
    finally:
        conn.close()
