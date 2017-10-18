import operator

f = open('http_access_log', 'r')

lineList = []
reqCount = {}
reqFileList = []

count = 0
for line in f:
	count+=1
	lineList.append(line)

for i in range(len(lineList)):
	listSplit = lineList[int(i)].split()
	try: reqFile = listSplit[6]
	except: pass
	reqFileList.append(reqFile)

for key in reqFileList:
	if key not in reqCount:
		reqCount[key] = 1
	else:
		if key in reqCount:
			reqCount[key] += 1

#print(reqCount)

mostRequested = max(reqCount.items(), key=operator.itemgetter(1))[0]
leastRequested = min(reqCount.items(), key=operator.itemgetter(1))[0]

print(str(mostRequested) + ' was requested the most, at ' + str(reqCount['index.html']) + ' times')
print(str(leastRequested) + ' was requested the least, at ' + str(reqCount['7512.map?159,276']) + ' times')

#print(reqCount['7512.map?159,276'])


#print(reqCount)
#print(reqFileList)
