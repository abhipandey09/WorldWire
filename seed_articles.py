import time
import logging
import database
import news_agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SeedArticles")

def seed():
    database.init_db()
    current_count = database.get_stats()['total_articles']
    logger.info(f"Current article count: {current_count}")
    
    target_categories = [
        "Technology",
        "Business",
        "Science",
        "World",
        "Climate",
        "Geopolitics",
        "Economy",
        "Politics",
        "Space & Aerospace",
        "Global Markets",
        "Energy Transition",
        "Biotech & Health",
        "International Diplomacy",
        "Artificial Intelligence",
        "Renewable Power",
        "World Affairs"
    ]
    
    needed = max(0, 25 - current_count)
    logger.info(f"Fetching {needed} new articles to achieve 25+ substantive dispatches...")
    
    count = 0
    for cat in target_categories:
        if current_count + count >= 26:
            break
        try:
            logger.info(f"Generating article for topic: {cat}...")
            res = news_agent.fetch_and_publish_news(target_category=cat)
            if res:
                count += 1
                logger.info(f"[{count}/{needed}] Published: {res.get('title')}")
            time.sleep(1) # respectful pause
        except Exception as e:
            logger.warning(f"Error fetching for {cat}: {e}")
            time.sleep(2)
            
    final_stats = database.get_stats()
    logger.info(f"Seeding completed. Total articles in DB: {final_stats['total_articles']}")

if __name__ == "__main__":
    seed()
