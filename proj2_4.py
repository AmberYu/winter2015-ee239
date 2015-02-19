import json
import ast

from collections import defaultdict
d=defaultdict(int)

tweets = []
for line in open('tweets.txt'):
	try:
		line_json = json.dumps(ast.literal_eval(line))
		tweets.append(json.loads(line_json))
	except:
		pass


retweet_count=[tweet['tweet']['retweet_count'] for tweet in tweets]
myset=set(retweet_count)
f = open('retweet_num.txt', 'w')
for item in myset:	
	print>>f, retweet_count.count(item), "tweets have ", item, "retweet"
f.close()




