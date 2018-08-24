import sys
import re
import os
import subprocess
import time
from sys import argv
Iterations=2


passc=0
failc=0
print("Iterations",Iterations)


def checkbluestate():
    os.system( "adb shell dumpsys bluetooth_manager > blogg.txt")
    bt=open("blogg.txt","r+")
    log=bt.read()
    print(log)
    bt.close()
    enabled=re.search("enabled: true", log , re.I)
    if enabled:
        return(True)
    else:
        return(False)
state=checkbluestate()
print(state)

def checkblueconnstate():
    os.system("adb shell dumpsys bluetooth_manager > bluetooth_log.txt")
    fp=open("bluetooth_log.txt","r+")
    bf=fp.read()
    ser=re.search("[BR/EDR]", bf)
    if ser:
         print("connected")
         return(True)
    else:
         return(False)
#connstate=checkblueconnstate()
#print(connstate)
def toggle():
    os.system("adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
    
def bluetooth():
    if state:
        print("enabled")
        checkblueconnstate()
    else:
        toggle()
        checkblueconnstate()
bluetooth()    

    
