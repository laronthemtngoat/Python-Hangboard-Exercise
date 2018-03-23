import time
import datetime

def repcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Rest for 3 seconds")
repcountdown(7)
