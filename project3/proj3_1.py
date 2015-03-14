import json
tweets = []
for line in open('tweets_#gohawks.txt'):
        tweets.append(json.loads(line))
tweets_num=len(tweets)
tweet_firstpost_date=[tweet['firstpost_date'] for tweet in tweets]
start=min(tweet_firstpost_date)
end=max(tweet_firstpost_date)
avg=tweets_num*3600/(end-start)

