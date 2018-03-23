import time
import datetime

def represtcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Start next rep")
represtcountdown(3)
time.sleep(5)
print "....."
