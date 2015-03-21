import os
import json
import datetime, time
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import random

def getPrediction(filename):
	tweets = []
	hashtag=filename[6:-4]
	f=open(filename)
	count = 0
	for line in f:

		if count>=0:
			try: 
				tweet=json.loads(line)
				tweets.append([tweet['firstpost_date'],tweet['tweet']['retweet_count'],tweet['tweet']['user']['followers_count'],tweet['tweet']['favorite_count'],tweet['tweet']['user']['friends_count'],tweet['metrics']['citations']['influential']])
				count=count+1
			except:
				print "error when reading tweets.txt"
		else:
			break
	f.close()

	time1 = int(time.mktime(datetime.datetime(2015,02,01, 8,00,0).timetuple()))
	time2 = int(time.mktime(datetime.datetime(2015,02,01, 20,00,0).timetuple()))

	tweet_firstpost_date=[tweet[0] for tweet in tweets]
	start=min(tweet_firstpost_date)
	end=max(tweet_firstpost_date)
	interval = (end-start)/3600


	time_window = [[0 for i in range(7)] for j in range(interval+2)]
	for i in range(len(tweets)):
		cur_time = tweets[i][0]


		index = (cur_time-start)/3600

		time_window[index][0] = time_window[index][0]+1
		time_window[index][1] = time_window[index][1]+tweets[i][1]
		# time_window[index][2] = max(time_window[index][2],tweets[i][2])
		time_window[index][2] = time_window[index][2]+tweets[i][3]
		# time_window[index][2] = time_window[index][2]+tweets[i][4]
		# time_window[index][2] = time_window[index][2]+tweets[i][5]
		time_window[index-1][3] = time_window[index][0]



	y=[]
	for i in range(interval+1):
		y.append(time_window[i][3])
	x=[]
	for i in range(interval+1):
		x.append(time_window[i][0:3])

	X = np.array(x)
	Y = np.array(y)

	params1=[ 0.65677283,  0.10038153,  0.12332733]
	params2=[ 0.83412658,  0.05784658,  0.06887859]
	params3=[ 1.49388183,  0.45498008,  0.57224698]
	
	f = open("Tweets_Prediction.txt","a")
	period = int(hashtag[-1])
	print>>f, hashtag+":"
	print hashtag+":"
	if period==1:
		print>>f, int(sum(params1*X[-1]))
		print int(sum(params1*X[-1]))
	if period==2:
		print>>f, int(sum(params2*X[-1]))
		print int(sum(params2*X[-1]))
	if period==3:
		print>>f, int(sum(params3*X[-1]))	
		print int(sum(params3*X[-1]))
	print>>f,""
	f.close()

	# f = open("model_params.txt","a")
	# print>>f,"model_params of "+hashtag
	# X1 = X[0:interval1+1]
	# Y1 = Y[0:interval1+1]
	# model = sm.OLS(X1, Y1)
	# results1 = model.fit()
	# print>>f, "period 1:"
	# print>>f, results1.params

	# X2 = X[interval1+1:interval2+1]
	# Y2 = Y[interval1+1:interval2+1]
	# model = sm.OLS(X2, Y2)
	# results2 = model.fit()
	# print>>f, "period 2:"
	# print>>f, results2.params

	# X3 = X[interval2:]
	# Y3 = Y[interval2:]
	# model = sm.OLS(X3, Y3)
	# results3 = model.fit()
	# print>>f, "period 3:"
	# print>>f, results3.params
	# f.close()

def Prediction():
    directory=os.getcwd()
    for file in os.listdir(directory+"/proj3"):
        if file.endswith('.txt'):
            getPrediction("proj3/"+file)

Prediction()



