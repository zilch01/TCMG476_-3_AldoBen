from datetime import datetime

f = open('http_access_log', 'r')

lineList = []
byMonth1994 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
byMonth1995 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

count = 0
for line in f:
	count += 1
	lineList.append(line)

for i in range(len(lineList)):
	splitLine = lineList[int(i)].split()

	try: date = splitLine[3][1:12]

	except: pass

	#print(date)
	try: formatted_date = datetime.strptime(date, "%d/%b/%Y")
	except: pass

	for key in byMonth1994:
		if formatted_date.isocalendar()[0] == 1994:
			if formatted_date.month == key:
				byMonth1994[formatted_date.month] += 1
		else: #1995
			if formatted_date.month == key:
                                byMonth1995[formatted_date.month] += 1
	#print(type(formatted_date.month))
	#print(byMonth1995)




months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
for i in range(12):
	print('1994: Requests made on '+ months[i]+ ': '+ str(byMonth1994[i+1]))

for i in range(12):
        print('1995: Requests made on '+ months[i]+ ': '+ str(byMonth1995[i+1]))

