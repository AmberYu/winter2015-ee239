
import os


if os.path.isfile('number_tags.txt'):
	os.remove('number_tags.txt')
if os.path.isfile('numbers_persecond.txt'):
	os.remove('numbers_persecond.txt')

# count the total number of tags
words = ['#SuperBowlXLIX',
'#Seahawks',
'#Patriots',
'#GoHawks',
'#GoPatriots',
'#Halftime',
'#superbowlcommercials']
number_tags = open('number_tags.txt', 'w')
max_query = '#SuperBowlXLIX'
max_count=0
for word in words:
	count=0
	for line in open("search_log.txt"):
		temp = line.split()
		if temp[0]==word:
			count=count+int(temp[8])
	if count>max_count:
		max_query = word
		max_count = count
	print>>number_tags, "total number of ",word,": ",count
number_tags.close()
line.close()
print max_query

# plot nunber per second of tags #SuperBowlXLIX
import urllib
import httplib
import json
import datetime, time

#########   create UNIX timestamps

start_date = datetime.datetime(2015,02,01, 18,50,0)
end_date = datetime.datetime(2015,02,01, 20,00,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

def tweets_persecond(mintime,query):
	#########   set query parameters
	params = urllib.urlencode({'apikey' : API_KEY, 'q' :query,
                           'mintime': str(mintime), 'maxtime': str(mintime+8),
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

	f=open('numbers_persecond.txt','a')
	print>>f, mintime,len(tweets),len(tweets)/8.0
	print mintime,len(tweets),len(tweets)/8.0


# every 8 seconds return a count
for i in range (mintime,maxtime-7,8):
	tweets_persecond(i,max_query)
