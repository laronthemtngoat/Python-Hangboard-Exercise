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

def represtcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Get to your next hold!")
represtcountdown(3)
time.sleep(5)
print "Start next rep!"

def setrestcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Start next set")
setrestcountdown(180)
