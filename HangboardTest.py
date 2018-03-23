import time
import datetime
holdList = ["Jug", "Sloper", "Big Pocket", "Big Crimp", "Medium Crimp", "Small Crimp", "2-finger Pocket", "Hard Pinch"]

def repcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Rest for 3 seconds")

def represtcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Get to your next hold!")

def setrestcountdown(n):
    while n > 0:
        print datetime.datetime.fromtimestamp(n).strftime('%M:%S')
        time.sleep(1)
        n = n - 1
        if n == 0:
            print ("Start next set")

#1st set
print "First Set!"
#1st rep
print holdList[0]
time.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[1]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[2]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[3]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[4]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[5]
time.sleep(5)
#6th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[6]
time.sleep(5)
#7th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[7]
time.sleep(5)
#8th rep
print "Start next rep!"
repcountdown(7)
print "3 minute rest!"
#3 minute Rest
setrestcountdown(180)

#2nd set- Big Pocket
print "Second Set!"
#1st rep
print holdList[2]
time.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[2]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[2]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[2]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[2]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[2]
time.sleep(5)
#6th rep
print "Start next rep!"
repcountdown(7)
print "3 minute rest!"
#3 minute Rest
setrestcountdown(180)

#3rd set- Medium Crimp
print "Third Set!"
#1st rep
print holdList[4]
time.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[4]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[4]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[4]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[4]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[4]
time.sleep(5)
#6th rep
print "Start next rep!"
repcountdown(7)
print "3 minute rest!"
#3 minute Rest
setrestcountdown(180)

#4th set- Sloper
print "Fourth Set!"
#1st rep
print holdList[1]
time.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[1]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[1]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[1]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[1]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[1]
time.sleep(5)
#6th rep
print "Start next rep!"
repcountdown(7)
print "3 minute rest!"
#3 minute Rest
setrestcountdown(180)

#5th set- Small Crimp
print "Fifth Set!"
#1st rep
print holdList[5]
time.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[5]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[5]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[5]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[5]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[5]
time.sleep(5)
#6th rep
print "Start next rep!"
repcountdown(7)
print "3 minute rest!"
#3 minute Rest
setrestcountdown(180)

#6th set- Jug
print "Sixth Set!"
#1st rep
print holdList[0]
time.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[0]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[0]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[0]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[0]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[0]
time.sleep(5)
#6th rep
print "Start next rep!"
repcountdown(7)
print "3 minute rest!"
#3 minute Rest
setrestcountdown(180)

#7th set- Hard Pinch & 2-Finger Pocket
print "Seventh Set!"
#1st rep
print "Left Hand: %s" % holdList[6]
print "Right Hand: %s" % holdList[7]
timer.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print "Left Hand: %s" % holdList[7]
print "Right Hand: %s" % holdList[6]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print "Left Hand: %s" % holdList[6]
print "Right Hand: %s" % holdList[7]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print "Left Hand: %s" % holdList[7]
print "Right Hand: %s" % holdList[6]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print "Left Hand: %s" % holdList[6]
print "Right Hand: %s" % holdList[7]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print "Left Hand: %s" % holdList[7]
print "Right Hand: %s" % holdList[6]
time.sleep(5)
#6th rep
print "Start next rep!"
repcountdown(7)
print "3 minute rest!"
#3 minute Rest
setrestcountdown(180)

#8th set- Big Crimp
print "Eighth AND Final Set!"
#1st rep
print holdList[3]
time.sleep(3)
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[3]
time.sleep(5)
#2nd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[3]
time.sleep(5)
#3rd rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[3]
time.sleep(5)
#4th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[3]
time.sleep(5)
#5th rep
print "Start next rep!"
repcountdown(7)
print "Rest!"
represtcountdown(3)
print holdList[3]
time.sleep(5)
#6th rep
print "Start last rep. You got this!"
repcountdown(7)
print "3 minute rest, then you are done!"
#3 minute Rest
setrestcountdown(180)
