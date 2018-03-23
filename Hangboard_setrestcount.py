import time
import datetime

def setrestcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Start next set")
setrestcountdown(180)
