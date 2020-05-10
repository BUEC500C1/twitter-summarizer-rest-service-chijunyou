import tweepy
def gettweets(searchterm,consumer_key,consumer_secret,access_key,access_secret):
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    termlength=len(searchterm)
    tweetlist=[]

    for tweets in api.search(q=searchterm, lang = 'en', result_type = 'recent', count = 200):
        tweetlist.append(tweets.text) 
    return tweetlist