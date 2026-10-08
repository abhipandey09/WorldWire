import logging
import threading
from datetime import datetime, timezone, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import database
import news_agent

logger = logging.getLogger("WorldWire.Scheduler")
logging.basicConfig(level=logging.INFO)

# Global singleton state
_scheduler = None
_scheduler_lock = threading.Lock()
_state = {
    "is_running": False,
    "last_run_time": None,
    "next_run_time": None,
    "status": "Initialized",
    "last_article_title": None,
    "last_error": None
}

def scheduled_job():
    """Job executed every 5 hours to fetch 1 hot topic world news article."""
    logger.info("Executing scheduled news fetch (5-hour interval)...")
    _state["status"] = "Fetching News..."
    try:
        res = news_agent.fetch_and_publish_news()
        _state["last_run_time"] = datetime.now(timezone.utc)
        _state["last_article_title"] = res.get("title")
        _state["status"] = "Active"
        _state["last_error"] = None
        logger.info(f"Scheduled news posted: {res.get('title')}")
    except Exception as e:
        logger.error(f"Error during scheduled news fetch: {e}")
        _state["status"] = "Error"
        _state["last_error"] = str(e)

def check_and_bootstrap_news():
    """Check if initial news is needed (e.g. if DB is empty or last article is >5 hours old)."""
    try:
        latest = database.get_latest_article()
        needs_fetch = False
        if not latest:
            logger.info("Database is empty. Triggering bootstrap news fetch...")
            needs_fetch = True
        else:
            published_at = latest.get("published_at")
            if published_at:
                now = datetime.now(timezone.utc)
                if (now - published_at) > timedelta(hours=5):
                    logger.info("Latest article is older than 5 hours. Triggering refresh fetch...")
                    needs_fetch = True

        if needs_fetch:
            # Run in a background thread so it doesn't block startup
            threading.Thread(target=scheduled_job, daemon=True).start()
    except Exception as e:
        logger.warning(f"Error checking news freshness on startup: {e}")

def start_scheduler():
    """Start the APScheduler background daemon if not already started."""
    global _scheduler
    with _scheduler_lock:
        if _scheduler is not None and _scheduler.running:
            return _scheduler

        _scheduler = BackgroundScheduler(daemon=True)
        # Schedule every 5 hours
        _scheduler.add_job(
            scheduled_job,
            trigger='interval',
            hours=5,
            id='worldwire_5hour_fetch',
            replace_existing=True,
            next_run_time=datetime.now(timezone.utc) + timedelta(hours=5)
        )
        _scheduler.start()
        _state["is_running"] = True
        _state["status"] = "Active"
        _state["next_run_time"] = datetime.now(timezone.utc) + timedelta(hours=5)
        logger.info("WorldWire 5-hour background scheduler started.")

        # Check if bootstrap news is needed
        check_and_bootstrap_news()

        return _scheduler

def trigger_manual_fetch():
    """Trigger an immediate asynchronous news fetch."""
    logger.info("Manual news fetch requested.")
    thread = threading.Thread(target=scheduled_job, daemon=True)
    thread.start()
    return thread

def get_scheduler_info():
    """Return current scheduler health and timing status."""
    global _scheduler
    next_run = None
    if _scheduler and _scheduler.running:
        job = _scheduler.get_job('worldwire_5hour_fetch')
        if job and job.next_run_time:
            next_run = job.next_run_time

    latest_db_article = None
    try:
        latest_db_article = database.get_latest_article()
    except Exception:
        pass

    return {
        "is_running": _scheduler.running if _scheduler else False,
        "status": _state["status"],
        "next_run_time": next_run or _state.get("next_run_time"),
        "last_run_time": _state.get("last_run_time") or (latest_db_article.get("published_at") if latest_db_article else None),
        "last_article_title": _state.get("last_article_title") or (latest_db_article.get("title") if latest_db_article else None),
        "last_error": _state.get("last_error")
    }

if __name__ == "__main__":
    start_scheduler()
    print("Scheduler running. Press Ctrl+C to exit.")
    import time
    while True:
        time.sleep(1)

