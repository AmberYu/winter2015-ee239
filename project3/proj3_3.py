import os
import json
import time
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

tweets = []
f=open('tweets_#superbowl.txt')
for line in f:
	try: 
		tweets.append(json.loads(line))
	except:
		print "error when reading tweets.txt"
tweet_firstpost_date=[tweet['firstpost_date'] for tweet in tweets]
start=min(tweet_firstpost_date)
end=max(tweet_firstpost_date)
interval = (end-start)/3600
time_window = [[0 for i in range(6)] for j in range(interval+2)]

for i in range(len(tweets)):
	cur_time = tweets[i]['firstpost_date']
	index = (cur_time-start)/3600
	time_window[index][0] = time_window[index][0]+1
	time_window[index][1] = time_window[index][1]+tweets[i]['metrics']['citations']['data'][0]['citations']
	time_window[index][2] = max(time_window[index][2],tweets[i]['tweet']['user']['followers_count'])
	time_window[index][3] = time_window[index][3]+tweets[i]['tweet']['favorite_count']
	time_window[index][4] = time_window[index][4]+tweets[i]['tweet']['user']['friends_count']
	time_window[index][5] = time_window[index][5]+tweets[i]['metrics']['citations']['influential']
y=[]
for i in range(interval+1):
	y.append(time_window[i+1][0])

del time_window[-1]
X = np.array(time_window)
Y = np.array(y)
model = sm.OLS(Y, X)
results = model.fit()

hashtag='#superbowl'

Time_Windows = open('Time_Windows_3#superbowl.txt', 'a')
print>>Time_Windows, hashtag
print>>Time_Windows, time_window
Time_Windows.close()

Linear_Regression_model = open('Linear_Regression_model_3#superbowl.txt', 'a')
print(results.summary())
y_predict=results.predict()
print>>Linear_Regression_model, hashtag
print>>Linear_Regression_model, results.summary()
Linear_Regression_model.close()


x1=[]
x3=[]
x5=[]

for i in range(interval+1):
	x1.append(time_window[i][0])
	x3.append(time_window[i][2])
	x5.append(time_window[i][4])

plt.figure(1)
plt.xlabel('Number of tweets')
plt.ylabel('Prediction')
plt.title('Prediction versus number of tweets for #superbowl')
plt.scatter(x1, y_predict, alpha=0.5)

plt.figure(2)
plt.xlabel('Maximum number of followers')
plt.ylabel('Prediction')
plt.title('Prediction versus maximum number of followers for #superbowl')
plt.scatter(x3, y_predict, alpha=0.5)

plt.figure(3)
plt.xlabel('number of friends')
plt.ylabel('Prediction')
plt.title('Prediction versus number of friends for #superbowl')
plt.scatter(x5, y_predict, alpha=0.5)

plt.show()

f.close()