import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv("UBvI1nU4561oul2xA8XdTjhgN")
    consumer_secret = os.getenv("VwyYjX8zlBz7KacqDlQy6VAoZarZPf3vQ70Zb5CR2p9MdQqBv4")
    access_token = os.getenv("907370106942042112-sNqyO61f4qa5aNtNDUV6rMjzQamioRO")
    access_token_secret = os.getenv("HLIQ4znIHVJCoqEJKwOMfhkwJCXYgN9yjhyfoAW6on2dN")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
