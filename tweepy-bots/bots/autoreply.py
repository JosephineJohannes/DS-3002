import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords):
    logger.info("Retrieving mentions of Formula 1")
    for tweet in api.search(q="Formula 1", lang="en", rpp=15):
        print(f"{tweet.user.name}:{tweet.text}")
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"])
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
