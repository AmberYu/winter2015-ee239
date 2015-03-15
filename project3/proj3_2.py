import os
import json
import time
import numpy as np
import statsmodels.api as sm

def getResults(filename):
	tweets = []
	f=open(filename)
	for line in f:
		try: 
			tweets.append(json.loads(line))
		except:
			print "error when reading tweets.txt"
	tweet_firstpost_date=[tweet['firstpost_date'] for tweet in tweets]
	start=min(tweet_firstpost_date)
	end=max(tweet_firstpost_date)
	interval = (end-start)/3600
	time_window = [[0 for i in range(5)] for j in range(interval+2)]

	for i in range(len(tweets)):
		cur_time = tweets[i]['firstpost_date']
		index = (cur_time-start)/3600
		time_window[index][0] = time_window[index][0]+1
		time_window[index][1] = time_window[index][1]+tweets[i]['tweet']['retweet_count']
		time_window[index][2] = time_window[index][2]+tweets[i]['author']['followers']
		time_window[index][3] = max(time_window[index][3],tweets[i]['tweet']['user']['followers_count'])
		cur_time = time.strftime('%H:%M:%S', time.gmtime(cur_time))
		time_window[index][4] = int(cur_time[0])*10+int(cur_time[1])
	y=[]
	for i in range(interval+1):
		y.append(time_window[i+1][0])

	del time_window[-1]
	X = np.array(time_window)
	Y = np.array(y)
	model = sm.OLS(Y, X)
	results = model.fit()

	hashtag=filename[7:-4]

	Time_Windows = open('Time_Windows', 'a')
	print>>Time_Windows, hashtag
	print>>Time_Windows, time_window
	Time_Windows.close()

	Linear_Regression_model = open('Linear_Regression_model', 'a')
	print(results.summary())

	print>>Linear_Regression_model, hashtag
	print>>Linear_Regression_model, results.summary()
	Linear_Regression_model.close()


	f.close()

def result():
    directory=os.getcwd()
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            getResults(file)

result()
