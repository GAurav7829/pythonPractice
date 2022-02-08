import _thread
import time

def TimeFunc(thread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print("%s: %s" %(thread, time.ctime(time.time())))

try:
    _thread.start_new_thread(TimeFunc, ("Thread NUmber 1", 1))
    _thread.start_new_thread(TimeFunc, ("Thread NUmber 2", 2))
except:
    print("Error: Unable to initaite thread")

while 1:
    pass