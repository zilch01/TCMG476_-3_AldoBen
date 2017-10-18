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

numUnsuccessful=0
for i in statusList:
	if 400 <= i <= 499:
		numUnsuccessful += 1

print('Percentage of unsuccessful requests: ' + str(100*(numUnsuccessful/726736.0)))
