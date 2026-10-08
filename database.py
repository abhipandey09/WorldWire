import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import logging

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise ValueError("DATABASE_URL environment variable is not set. Please specify it in .env")

# Ensure clean connection string if channel_binding causes SSL syscall issues
if "channel_binding=require" in DB_URL:
    DB_URL = DB_URL.replace("&channel_binding=require", "").replace("?channel_binding=require", "?")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WorldWire.DB")

def get_connection(retries: int = 4, delay: float = 2.0):
    """Get a connection to Neon PostgreSQL with automatic retries for serverless cold-starts."""
    last_err = None
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(DB_URL, connect_timeout=15)
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
    """Initialize database tables and indexes."""
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

    CREATE INDEX IF NOT EXISTS idx_news_published_at ON news_articles (published_at DESC);
    CREATE INDEX IF NOT EXISTS idx_news_category ON news_articles (category);
    CREATE UNIQUE INDEX IF NOT EXISTS idx_news_title ON news_articles (title);
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()
        logger.info("Database initialized successfully.")
    finally:
        conn.close()

@execute_with_retry
def insert_article(article_data: dict) -> bool:
    """Insert a new article into the database, ignoring duplicates."""
    query = """
    INSERT INTO news_articles (
        title, summary, content, category, hot_topic_tag, 
        image_url, source_name, source_url, region, published_at
    ) VALUES (
        %(title)s, %(summary)s, %(content)s, %(category)s, %(hot_topic_tag)s,
        %(image_url)s, %(source_name)s, %(source_url)s, %(region)s, %(published_at)s
    )
    ON CONFLICT (title) DO NOTHING
    RETURNING id;
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, article_data)
            row = cur.fetchone()
            conn.commit()
            return row is not None
    finally:
        conn.close()

@execute_with_retry
def get_articles(limit: int = 50, category: str = None, search: str = None):
    """Retrieve articles ordered by latest published_at."""
    conditions = []
    params = {}
    
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
           image_url, source_name, source_url, region, published_at, created_at
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
def get_latest_article():
    """Retrieve the single most recent article."""
    query = """
    SELECT * FROM news_articles
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
