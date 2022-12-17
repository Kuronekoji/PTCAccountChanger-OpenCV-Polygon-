#!/usr/bin/env python3
#Referral Code: #
#Pixel 2XL IP: #

from cv2 import COLOR_BGR2GRAY, threshold
from ppadb.client import Client

import time
from datetime import datetime

import os
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

os.system("cls")


curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("Start time of execution: " + curTime)


RESTART_COUNT = 0
ACC_NUM = 0
BALL_X = 0
BALL_Y = 0
RESPONSE = input("Enter running config (oneraid / new): ")


def polyStart():

    for counter in range(2):
        device.shell('input touchscreen tap 1122 2781') #Switch to polygon

#Stop polygon and close pokemon go
def polyStop():
    for counter in range(2):
        device.shell('input touchscreen tap 1122 2781')

    device.shell('input touchscreen tap 696 1005') #Stop polygon

    device.shell('input touchscreen tap 1122 2781') #Open app view

    device.shell('input touchscreen swipe 50 2000 50 300 1000') #Close pokemon go

    device.shell('input touchscreen tap 696 1005') #Bring polygon into focus


def signIn():
    global ACC_NUM

    device.shell('input touchscreen tap 706 1932') #Returning Player

    time.sleep(5)

    device.shell('input touchscreen tap 668 1646') #Login with PTC

    time.sleep(5)

    device.shell('input touchscreen tap 640 1128') #Username textbox
    if (ACC_NUM == 0):
        device.shell('input touchscreen text USERNAME')
        print("Account #: " , ACC_NUM)
    elif (ACC_NUM == 1):
        device.shell('input touchscreen text USERNAME')
        print("Account #: " , ACC_NUM)
    elif (ACC_NUM == 2):
        device.shell('input touchscreen text USERNAME')
        print("Account #: " , ACC_NUM)
    elif (ACC_NUM == 3):
        device.shell('input touchscreen text USERNAME')
        print("Account #: " , ACC_NUM)
    elif (ACC_NUM == 4):
        device.shell('input touchscreen text USERNAME')
        print("Account #: " , ACC_NUM)


    device.shell('input touchscreen tap 1343 2577') #Accept
    ACC_NUM = ACC_NUM + 1

    device.shell('input touchscreen tap 700 1370') #Password textbox
    device.shell('input touchscreen text YOURPASSWORD')
    device.shell('input touchscreen tap 1343 2577')

    device.shell('input touchscreen tap 728 1602') #Sign in



def signInMain():
    device.shell('input touchscreen tap 706 1932') #Returning Player

    


def signOut():
    for counter in range(3):
        device.shell('input touchscreen swipe 1000 2000 1000 1100 300') #Scroll 3 times down settings
        time.sleep(1)

    time.sleep(5)
    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)


    img = cv.imread('screen.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    template = cv.imread('target.png',0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    location = np.where(res >= threshold)

    try:
        for pt in zip(*location[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imwrite('res.png', img)
        x = pt[0]
        y = pt[1]
        center_X = x + 0.5 * w
        center_Y = y + 0.5 * w

        center_X = int(center_X)
        center_Y = int(center_Y)
        print("Sign out found at: (" + str(center_X) + ", " + str(center_Y) + ")")

        device.shell('input touchscreen tap ' + str(center_X) + ' ' + str(center_Y))

        time.sleep(2)

        device.shell('input touchscreen tap 726 1341') #Confirm Sign out

    except UnboundLocalError:
        pass

def settingsSignOut():
    device.shell('input touchscreen tap 750 2500') #Open menu

    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)


    img = cv.imread('screen.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    template = cv.imread('settings.png',0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    location = np.where(res >= threshold)

    try:
        for pt in zip(*location[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imwrite('settingsResult.png', img)
        x = pt[0]
        y = pt[1]
        center_X = x + 0.5 * w
        center_Y = y + 0.5 * h

        center_X = int(center_X)
        center_Y = int(center_Y)
        print("Settings found at: (" + str(center_X) + ", " + str(center_Y) + ")")

        time.sleep(2)

        device.shell('input touchscreen tap ' + str(center_X) + ' ' + str(center_Y))

        time.sleep(2)

    except UnboundLocalError:
        print("Settings not found. Retrying...")
        device.shell('input touchscreen tap 750 2500') #Attempt open menu
        settingsSignOut()
        pass





def ballCheck():
    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)


    img = cv.imread('screen.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    template = cv.imread('ballTarget.png',0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    location = np.where(res >= threshold)

    try:
        for pt in zip(*location[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imwrite('ballResult.png', img)
        x = pt[0]
        y = pt[1]
        center_X = x + 0.5 * w
        center_Y = y + 0.5 * h

        center_X = int(center_X)
        center_Y = int(center_Y)
        print("Pogo ball at: (" + str(center_X) + ", " + str(center_Y) + ") " + "No notifications to skip.")

    except UnboundLocalError:
        print("Ball not found. Retrying...")
        device.shell('input touchscreen tap 750 2500') #Attempt open menu
        #settingsCheck()
        ballCheck()
        pass


def raidSleep():
    curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Current Time: " , curTime)

    print("Waiting to finish raid.")
    time.sleep(120)
    notifCheck()


def notifCheck():
    global BALL_X, BALL_Y

    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)


    curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Notification Check Time: ", curTime)

    count = [0, 0, 0, 0, 0, 0]
    img = cv.imread('screen.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    templates = [cv.imread('ballTarget.png', 0), cv.imread('settings.png', 0), cv.imread('walkReward.png', 0), cv.imread('tradeTarget.png', 0), cv.imread('newsTarget.png', 0), cv.imread('raidTarget.png', 0)]
    w1,h1=templates[0].shape[::-1]
    w2,h2=templates[1].shape[::-1]
    w3,h3=templates[2].shape[::-1]
    w4,h4=templates[3].shape[::-1]
    w5,h5=templates[4].shape[::-1]
    w6,h6=templates[5].shape[::-1]

    resultBall=cv.matchTemplate(img_gray, templates[0], cv.TM_CCOEFF_NORMED)
    resultSettings=cv.matchTemplate(img_gray, templates[1], cv.TM_CCOEFF_NORMED)
    resultReward=cv.matchTemplate(img_gray, templates[2], cv.TM_CCOEFF_NORMED)
    resultTrade=cv.matchTemplate(img_gray, templates[3], cv.TM_CCOEFF_NORMED)
    resultNews=cv.matchTemplate(img_gray, templates[4], cv.TM_CCOEFF_NORMED)
    resultRaid=cv.matchTemplate(img_gray, templates[5], cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    locBall = np.where(resultBall>=threshold)
    locSettings = np.where(resultSettings>=threshold)
    locReward = np.where(resultReward>=threshold)
    locTrade = np.where(resultTrade>=threshold)
    locNews = np.where(resultNews>=threshold)
    locRaid = np.where(resultRaid>=threshold)


    try:
        for pt1 in zip(*locTrade[::-1]):
            cv.rectangle(img, pt1, (pt1[0] + w1, pt1[1] + h1), (0, 0, 255), 2)
            count[0] = count[0] + 1 

        cv.imwrite('tradeResult.png', img)
        x = pt1[0]
        y = pt1[1]
        center_X = x + 0.5 * w1
        center_Y = y + 0.5 * h1

        center_X = int(center_X)
        center_Y = int(center_Y)

        print("Trade found at: (" + str(center_X) + ", " + str(center_Y) + ")" + " Skipping...")
        device.shell('input touchscreen tap 709 2128') #Skip Trades

    except UnboundLocalError:
        print("Trade not found. Trying next...")
        pass

    try:
        for pt2 in zip(*locNews[::-1]):
            cv.rectangle(img, pt2, (pt2[0] + w2, pt2[1] + h2), (0, 0, 255), 2)
            count[0] = count[0] + 1 

        cv.imwrite('newsResult.png', img)
        x = pt1[0]
        y = pt1[1]
        center_X = x + 0.5 * w1
        center_Y = y + 0.5 * h1

        center_X = int(center_X)
        center_Y = int(center_Y)

        print("News found at: (" + str(center_X) + ", " + str(center_Y) + ")" + " Skipping...")
        device.shell('input touchscreen tap 712 2584') #Dismiss News
        

    except UnboundLocalError:
        print("No news found. Trying next.")
        time.sleep(2)
        pass

    try:
        for pt3 in zip(*locSettings[::-1]):
            cv.rectangle(img, pt3, (pt3[0] + w3, pt3[1] + h3 ), (255, 0 ,0), 2)
            count[2] = count[2] + 1

        cv.imwrite('settingsResult.png', img)
        x = pt3[0]
        y = pt3[1]
        center_X = x + 0.5 * w3
        center_Y = y + 0.5 * h3

        center_X = int(center_X)
        center_Y = int(center_Y)
        print("Settings found at: (" + str(center_X) + ", " + str(center_Y) + ")" + " No Notifications.")

        time.sleep(2)

        device.shell('input touchscreen tap ' + str(BALL_X) + ' ' + str(BALL_Y)) #Close settings

        time.sleep(2)

    except UnboundLocalError:
        print("Settings not found. Trying next...")
        time.sleep(2)
        pass

    try:

        for pt4 in zip(*locReward[::-1]):
            cv.rectangle(img, pt4, (pt4[0] + w4, pt4[1 ]+ h4), (0, 0, 255), 2)
            count[3] = count[3] + 1

        cv.imwrite('walkResult.png', img)
        x = pt4[0]
        y = pt4[1]
        center_X = x + 0.5 * w4
        center_Y = y + 0.5 * h4

        center_X = int(center_X)
        center_Y = int(center_Y)

        print("Rewards found at: (" + str(center_X) + ", " + str(center_Y) + ")")
        device.shell('input touchscreen tap 719 2341') #Close rewards

    except UnboundLocalError:
        print("Walking reward not found. Trying next...")
        time.sleep(2)
        pass


    try:

        for pt5 in zip(*locRaid[::-1]):
            cv.rectangle(img, pt5, (pt5[0] + w5, pt5[1 ]+ h5), (0, 0, 255), 2)
            count[4] = count[4] + 1

        cv.imwrite('raidResult.png', img)
        x = pt5[0]
        y = pt5[1]
        center_X = x + 0.5 * w5
        center_Y = y + 0.5 * h5

        center_X = int(center_X)
        center_Y = int(center_Y)

        print("Raid found at: (" + str(center_X) + ", " + str(center_Y) + ")")
        raidSleep()

    except UnboundLocalError:
        print("Not in raid, continue checks...")
        time.sleep(2)
        pass

    try:
        for pt6 in zip(*locBall[::-1]):
            cv.rectangle(img, pt6, (pt6[0] + w6, pt6[1] + h6 ), (0, 255, 0), 2)
            count[5] = count[5] + 1

        cv.imwrite('ballResult.png', img)
        x = pt6[0]
        y = pt6[1]
        center_X = x + 0.5 * w6
        center_Y = y + 0.5 * h6

        center_X = int(center_X)
        center_Y = int(center_Y)

        print("Pogo ball at: (" + str(center_X) + ", " + str(center_Y) + ") " + "No notifications to skip.")
        device.shell("input touchscreen tap " + str(center_X) + " " + str(center_Y))

        BALL_X = int(center_X)
        BALL_Y = int(center_Y)

    except UnboundLocalError:
        print("Ball not found. Sending to ballCheck to confirm")
        time.sleep(2)
        ballCheck()
        pass


def importCheck():

    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)


    img = cv.imread('screen.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    template = cv.imread('importTarget.png',0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    location = np.where(res >= threshold)

    try:
        for pt in zip(*location[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imwrite('importResult.png', img)
        x = pt[0]
        y = pt[1]
        center_X = x + 0.5 * w
        center_Y = y + 0.5 * h

        center_X = int(center_X)
        center_Y = int(center_Y)
        print("Import found at: (" + str(center_X) + ", " + str(center_Y) + ")")

        device.shell("input touchscreen tap " + str(center_X) + " " + str(center_Y))

    except UnboundLocalError:
        print("Import not found. Trying again...")
        importCheck()
        pass

def raidConfigCheck():

    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)


    img = cv.imread('screen.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    template = cv.imread('configRaidsTarget.png',0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    location = np.where(res >= threshold)

    try:
        for pt in zip(*location[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imwrite('configRaidsResult.png', img)
        x = pt[0]
        y = pt[1]
        center_X = x + 0.5 * w
        center_Y = y + 0.5 * h

        center_X = int(center_X)
        center_Y = int(center_Y)
        print("Config found at: (" + str(center_X) + ", " + str(center_Y) + ")")

        device.shell("input touchscreen tap " + str(center_X) + " " + str(center_Y))

    except UnboundLocalError:
        print("Config not found. Trying again...")
        importCheck()
        pass


def mainConfigCheck():
    global MAIN_CONFIG_X, MAIN_CONFIG_Y 

    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)


    img = cv.imread('screen.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    template = cv.imread('configMineTarget.png',0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    location = np.where(res >= threshold)

    try:
        for pt in zip(*location[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imwrite('configMineResult.png', img)
        x = pt[0]
        y = pt[1]
        center_X = x + 0.5 * w
        center_Y = y + 0.5 * h

        center_X = int(center_X)
        center_Y = int(center_Y)
        print("Config found at: (" + str(center_X) + ", " + str(center_Y) + ")")

        device.shell("input touchscreen tap " + str(center_X) + " " + str(center_Y))

        MAIN_CONFIG_X = center_X
        MAIN_CONFIG_Y = center_Y

    except UnboundLocalError:
        print("Config not found. Trying again...")
        importCheck()
        pass
    

def polyConfigMain():

    polyStop() #Stop polygon

    device.shell('input touchscreen tap ') #Open polygon settings

    for counter in range(5):
        device.shell('input touchscreen swipe 1000 2000 1000 1100 300') #Scroll 5 times down polygon settings
        time.sleep(1)

    importCheck() #Look for import button
    
    time.sleep(5)

    device.shell('input touchscreen ' + str(MAIN_CONFIG_X) + " " + str(MAIN_CONFIG_Y)) #Choose main config
    time.sleep(2)
    device.shell('input touchscreen 321 2813') #Back to poly main screen
    time.sleep(1)
    device.shell('input touchscreen tap 702 771') #Start polygon



if RESPONSE == "oneraid":

    while True:

        polyStop()  
        device.shell('input touchscreen tap 750 2875') #Home button
        device.shell('input touchscreen tap 420 642') #Open pokemon go

        time.sleep(50) #Wait for pokemon to boot

        device.shell('input touchscreen tap 722 2010') #Dismiss opening notice

        time.sleep(15) #Wait 

        notifCheck()

        settingsSignOut() #Check to see if settings is visible for signout

        time.sleep(5)

        signOut()

        time.sleep(15) #Wait for logout

        signIn()

        time.sleep(15)

        polyStart()
        RESTART_COUNT = 0
        device.shell('input touchscreen tap 702 771') #Start polygon
        RESTART_COUNT = RESTART_COUNT + 1
        curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Initial reset: " , RESTART_COUNT , " | Time of reset: " , curTime)
        time.sleep(100) #Wait 1min 20sec for full game boot

        notifCheck()

        print("------------------------WAIT------------------------")
        time.sleep(120) #Play for a bit

        notifCheck()

        time.sleep(5)

        polyConfigMain() #Switch to main account config

        signOut() #Sign out

        time.sleep(15) #wait for logout

        #polyStop()
        #time.sleep(2)
        #device.shell('input touchscreen tap 702 771') #Start polygon
        RESTART_COUNT = RESTART_COUNT + 1
        curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Reset: " , RESTART_COUNT , " | Time of reset: " , curTime)

        time.sleep(100) #Wait 1min 20 sec for full game boot

        notifCheck()

        print("------------------------WAIT------------------------")
        time.sleep(300) #5 minute wait

        notifCheck()

        #print("------------------------WAIT------------------------")
        #time.sleep(300) #5 minute wait

        #notifCheck()

        #time.sleep(300) #5 minutes to battle unown
        curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Current Time: " , curTime)
        print("5 minute warning")
        print("------------------------WAIT------------------------")
        #time.sleep(300) #Extra 5 minutes to do whatever, total 10 mins, total runtime est ~18min
        print("------------------------Changing accounts------------------------")

        if (ACC_NUM == 5):
            False

elif RESPONSE == "new":

    while True:

        polyStop()  
        device.shell('input touchscreen tap 750 2875') #Home button
        device.shell('input touchscreen tap 420 642') #Open pokemon go

        time.sleep(50) #Wait for pokemon to boot

        device.shell('input touchscreen tap 722 2010') #Dismiss opening notice

        time.sleep(15) #Wait 

        notifCheck()

        settingsSignOut() #Check to see if settings is visible for signout

        time.sleep(5)

        signOut()

        time.sleep(15) #Wait for logout

        signIn()

        time.sleep(15)

        polyStart()
        RESTART_COUNT = 0
        device.shell('input touchscreen tap 702 771') #Start polygon
        RESTART_COUNT = RESTART_COUNT + 1
        curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Initial reset: " , RESTART_COUNT , " | Time of reset: " , curTime)
        time.sleep(100) #Wait 1min 20sec for full game boot

        notifCheck()

        print("------------------------WAIT------------------------")
        time.sleep(120) #Play for a bit | 2 min

        notifCheck()

        #Login to main account and switch config here

        polyStop()
        time.sleep(2)
        device.shell('input touchscreen tap 702 771') #Start polygon
        RESTART_COUNT = RESTART_COUNT + 1
        curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Reset: " , RESTART_COUNT , " | Time of reset: " , curTime)

        time.sleep(100) #Wait 1min 20 sec for full game boot

        notifCheck()

        print("------------------------WAIT------------------------")
        time.sleep(300) #5 minute wait

        notifCheck()

        #print("------------------------WAIT------------------------")
        #time.sleep(300) #5 minute wait

        #notifCheck()

        curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Current Time: " , curTime)
        print("5 minute warning")
        print("------------------------WAIT------------------------")
        time.sleep(300) #Extra 5 minutes to do whatever, total 10 mins, total runtime per account est ~18min
        print("------------------------Changing accounts------------------------")

        if (ACC_NUM == 5):
            False