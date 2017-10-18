from datetime import datetime

f = open('http_access_log', 'r')

lineList = []
byWeek1994 = {}
byWeek1995 = {}
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

	#byWeek[formatted_date.weekday()] += 1
	iso_tuple = formatted_date.isocalendar()
	#print(iso_tuple[0])
	for key in range(53):
		if 1994 == iso_tuple[0]:
			if key not in byWeek1994.keys():
				byWeek1994[key] = 0
			else:
				if key == iso_tuple[1]:
					byWeek1994[key] += 1
		if 1995 == iso_tuple[0]:
                        if key not in byWeek1995.keys():
                                byWeek1995[key] = 0
                        else:
                                if key == iso_tuple[1]:
                                        byWeek1995[key] += 1


#print(byWeek1994)
#print(byWeek1995)

week = []
string='week'
for i in range(53):
	weekNum = string + ' ' + str(i)
	week.append(weekNum)

for key in range(53):
		print('1994: Requests made on '+ week[key]+ ': '+ str(byWeek1994[key]))
for key in range(53):
		print('1995: Requests made on  '+ week[key]+ ': '+ str(byWeek1995[key]))

