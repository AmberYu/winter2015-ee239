f=open('retweet_num.txt','r')
twtnum=[]
k=[]
for line in f:
     data=line.split()
     k.append(data[3])
     twtnum.append(data[0]) 

X=map(int,k)
Y=map(int,twtnum)
y_sorted = [y for (x,y) in sorted(zip(X,Y))] 
X.sort()
m=map(str,X)

x=range(1,77)
import matplotlib.pyplot as plt
import numpy as np
ax=plt.subplot(111)
ax.bar(x,y_sorted,width=0.5)
ax.set_xticks(map(lambda i: i, range(1,len(Y)+1)))
ax.set_xticklabels(m,rotation=90, rotation_mode="anchor", ha="right",fontsize=8)
plt.title('The Number of Retweets in Linear Scale')
plt.xlabel('The Retweeted Time')
plt.ylabel('The Number of Retweeted Tweets')
plt.show()

##plot in log-log scale

import math

z=map(float,y_sorted)
n=map(float,X)
twtlog=[]
klog=[]
for i in z:
    twtlog.append(math.log10(i))

for i in n:    
    klog.append(math.log10(i))
myFormattedList = [ '%.2f' % elem for elem in klog ]
m=map(str,myFormattedList)

ax=plt.subplot(111)
ax.bar(x,twtlog,width=0.5)
ax.set_xticks(map(lambda i: i, range(1,len(Y)+1)))
ax.set_xticklabels(m,rotation=90, rotation_mode="anchor", ha="right",fontsize=8)
plt.title('The Number of Retweets in log-log Scale')
plt.xlabel('The Retweeted Time')
plt.ylabel('The Number of Retweeted Tweets')
plt.show()


