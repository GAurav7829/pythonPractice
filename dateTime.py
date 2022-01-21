import time
import calendar

#ticks
var1 = time.time()
print(var1)

#local time
localTime = time.localtime(time.time())
print(localTime)
print(str(localTime.tm_hour)+':'+str(localTime.tm_min)+':'+str(localTime.tm_sec))

#Formatted time
localTime1 = time.asctime(time.localtime(time.time()))
print(localTime1)

#Calender
calenderVar = calendar.month(2021,1)
print(calenderVar)