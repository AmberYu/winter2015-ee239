second = file('numbers_persecond_Patriots.txt')
first = file('numbers_persecond_SuperBowlXLIX.txt')
f = open('first_second_correlation.txt','w')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
	line1 = first.readline()
	line2 = second.readline()
	if len(line1) == 0: # Zero length indicates EOF
		break
	rate1=line1.split()
	rate2=line2.split()
	if float(rate2[2])==0.0:
		rate2[2]=0.001
	print>>f, rate1[0],"  tag1: ",rate1[2],"  tag2: ",rate2[2], "  tag1/tag2: ",float(rate1[2])/float(rate2[2])

f.close() # close the file
first.close()
second.close()
