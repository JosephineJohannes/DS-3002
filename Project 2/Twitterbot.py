import tweepy

# Authenticating to Twitter
consumerKey = 'M0dGAYkkINWEkq5sPQqQMKh2w'
consumerSecret = 'VvL5aN72e6BlkbSk1T6DbWZHnnhSv5iCY56xPOShrp9cXlGrRa'
accessToken = '907370106942042112-yQdqY74cmG0L4jh9TMLKFnd4FWyUXpw'
accessTokenSecret = 'AHpvwZoGgj06Q967ItczcgW7h7OsSjlhlIyLLZonYcqh7'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

# Creating API Object
api = tweepy.API(auth)
