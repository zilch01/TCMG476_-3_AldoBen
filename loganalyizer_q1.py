
file = open("http_access_log", "r")
#print file.read()
count = 0
for line in file:
        count+=1
print ("Total requests made: ",  count)
