import tweepy

# Authenticating to Twitter
auth = tweepy.OAuthHandler("UBvI1nU4561oul2xA8XdTjhgN", "VwyYjX8zlBz7KacqDlQy6VAoZarZPf3vQ70Zb5CR2p9MdQqBv4")
auth.set_access_token("907370106942042112-D86dU6PMvGlupuU3cHXLgQELjGXidi7",
                      "HLIQ4znIHVJCoqEJKwOMfhkwJCXYgN9yjhyfoAW6on2dN")

# Creating API Object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    api = tweepy.API(auth, wait_on_rate_limit=True)
    for tweet in api.search(q="Formula 1", lang="en", rpp=15):
        print(f"{tweet.user.name}:{tweet.text}")
except:
    print("Error during authentication")
