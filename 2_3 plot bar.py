import matplotlib.pyplot as plt
import numpy as np
names = ['#SuperBowlXLIX','#Seahawks','#Patriots','#GoHawks','#GoPatriots','#Halftime','#superbowlcommercials']
y= [51897,23837,33128,6614,4050,1326,1979]
ax=plt.subplot(111)
width=0.7
bins = map(lambda x: x-width/2,range(1,len(y)+1))
ax.bar(bins,y,width=width)
ax.set_xticks(map(lambda x: x, range(1,len(y)+1)))
ax.set_xticklabels(names,rotation=20, rotation_mode="anchor", ha="right")
plt.xlabel('HashTag')
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets For Each HashTag')
plt.show()

