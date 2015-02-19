import json
import ast

from collections import defaultdict
d=defaultdict(int)

tweets = []
for line in open('tweets.txt'):
	try:
		tweets.append(json.loads(line))
	except:
		pass


retweet_count=[tweet['tweet']['retweet_count'] for tweet in tweets]
myset=set(retweet_count)
f = open('retweet_num.txt', 'w')
for item in myset:	
	print>>f, retweet_count.count(item), "tweets have ", item, "retweet"
f.close()




