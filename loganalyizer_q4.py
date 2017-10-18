import re

f = open('http_access_log', 'r')

lineList = []
statusList = []

count = 0
for line in f:
	count += 1
	lineList.append(line)

for i in range(len(lineList)):
	splitLine = lineList[int(i)].split()

	try: status = splitLine[8]
	except: pass

	try: statusInt = int(status)
	except: pass

	statusList.append(statusInt)

numSuccessful=0
for i in statusList:
	if 300 <= i <= 399:
		numSuccessful += 1

#numSuccessful means successfully redirected.

print('Percentage of redirected requests: ' + str(100*(numSuccessful/726736.0)))

