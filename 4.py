import urllib
import httplib
import json
import datetime, time
import os


if os.path.isfile('tweets.txt'):
	os.remove('tweets.txt')

#########   create UNIX timestamps

start_date = datetime.datetime(2015,02,01, 18,50,0)
end_date = datetime.datetime(2015,02,01, 20,00,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))




API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

from collections import defaultdict
d=defaultdict(int)

def tweets(mintime,maxtime,query):
	#########   set query parameters
	params = urllib.urlencode({'apikey' : API_KEY, 'q' :query,
                           'mintime': str(mintime), 'maxtime': str(maxtime),
                           'new_only': '1', 'include_metrics':'1', 'limit': 500})

#########   create and send HTTP request
	req_url = url + '?' + params
	req = httplib.HTTPConnection(host)
	req.putrequest("GET", req_url)
	req.putheader("Host", host)
	req.endheaders()
	req.send('')


#########   get response and print out status
	resp = req.getresponse()
	# print resp.status, resp.reason


#########   extract tweets
	resp_content = resp.read()
	ret = json.loads(resp_content)
	tweets = ret['response']['results']['list']

	if len(tweets)<500:
        f=open('tweets.txt','a')
        for item in tweets:
            print>>f, item
        f.close()

        retweet_count=[tweet['tweet']['retweet_count'] for tweet in tweets]
        myset=set(retweet_count)
        for item in myset:
            d[item]+=retweet_count.count(item)

	return len(tweets)

def split_tweets(mintime,maxtime,query):
	len  = tweets(mintime,maxtime,query)
	if len ==500:
		if(mintime<maxtime):
			mid = (mintime+maxtime)/2
			split_tweets(mintime,mid,query)
			split_tweets(mid,maxtime,query)
	else:
		
		timefrom = time.localtime(mintime)
		timeto = time.localtime(maxtime)
queries = ['#SuperBowlXLIX',
'#Seahawks',
'#Patriots',
'#GoHawks',
'#GoPatriots',
'#Halftime',
'#superbowlcommercials']

for query in queries:
	split_tweets(mintime,maxtime,query)



