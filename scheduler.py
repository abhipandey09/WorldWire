import logging
import threading
from datetime import datetime, timezone, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import job_scraper
import job_store

logger = logging.getLogger("WorkWire.Scheduler")
logging.basicConfig(level=logging.INFO)

_scheduler = None
_scheduler_lock = threading.Lock()
_state = {
    "is_running": False,
    "last_run_time": None,
    "status": "Initialized",
    "last_count": 0,
    "last_error": None
}

def scheduled_job():
    """Daily/12-hour job execution to scrape new vacancies for admin review."""
    logger.info("Executing scheduled job scraping cycle...")
    _state["status"] = "Scraping Job Feeds..."
    try:
        count = job_scraper.run_job_scraping_cycle()
        _state["last_run_time"] = datetime.now(timezone.utc)
        _state["last_count"] = count
        _state["status"] = "Active"
        _state["last_error"] = None
        logger.info(f"Scheduled scraping completed: {count} positions added to pending review queue.")
    except Exception as e:
        logger.error(f"Error during scheduled job scraping: {e}")
        _state["status"] = "Error"
        _state["last_error"] = str(e)

def check_and_bootstrap_jobs():
    """Verify jobs data exists and bootstrap scraping if needed."""
    try:
        stats = job_store.get_job_stats()
        last_str = stats.get("last_fetched_at")
        needs_fetch = False
        if not last_str:
            needs_fetch = True
        else:
            try:
                last_dt = datetime.fromisoformat(last_str)
                if (datetime.now(timezone.utc) - last_dt) > timedelta(hours=24):
                    needs_fetch = True
            except Exception:
                needs_fetch = True

        if needs_fetch:
            threading.Thread(target=scheduled_job, daemon=True).start()
    except Exception as e:
        logger.warning(f"Error checking jobs freshness on startup: {e}")

def start_scheduler():
    global _scheduler
    with _scheduler_lock:
        if _scheduler is not None and _scheduler.running:
            return _scheduler

        _scheduler = BackgroundScheduler(daemon=True)
        # Schedule scraping cycle every 12 hours
        _scheduler.add_job(scheduled_job, 'interval', hours=12, id='job_scraper_daemon')
        _scheduler.start()
        _state["is_running"] = True
        _state["status"] = "Active"
        logger.info("WorkWire background job scraper scheduler started (12-hour interval).")

        check_and_bootstrap_jobs()
        return _scheduler

def get_scheduler_status():
    return _state
