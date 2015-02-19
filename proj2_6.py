import json
def parser(i):
	tweets = []
	for line in open('tweets.txt'):
		try: 
			tweets.append(json.loads(line))
		except:
			print "error when reading tweets.txt"

	tweet_firstpost_date = tweets[i]['firstpost_date']
	tweet_text = tweets[i]['tweet']['text']
	tweet_retweets = tweets[i]['tweet']['retweet_count'] 
	tweet_author = tweets[i]['author']['name'] 

	print>>f, "post date: ",json.dumps(tweet_firstpost_date)
	print>>f, "text: ",json.dumps(tweet_text)
	print>>f, "retweets number: ",json.dumps(tweet_retweets)
	print>>f, "user name: ",json.dumps(tweet_author)

f = open ('parser.txt','w')
parser(0)
f.close()
