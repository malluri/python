import re
import os
import datetime
def open():
    k=0
    while(os.system("adb shell getprop sys.boot_completed")):  
        k=0
def closed():
    k=0
    while(os.system("adb shell getprop sys.boot_completed")==0):
        k=0
    
def batterycheck_first(mode):
    b=mode
    os.system("adb shell dumpsys battery > batteryyyy.txt")
    fp=open("/Users/malluri/Documents/script/batteryyyy.txt","r+")
    content=fp.readlines()
    #print(content)
    for line in content:
        if(b in line ):
            print(line)
            for j in line.split():
                #print(j)
                now = datetime.datetime.now()
                su=float((60*now.hour)+now.minute+(now.second/60))
                if(j.isdigit()):
                    print("during {0}  battery level is{1}".format(datetime.datetime.now(),j))
                    global level
                    level1=j
                    print(level1)
                    global time
                    time1=su
                    print(time1)
batterycheck_first("level")                    
"""                    
def batterycheck_sec(mode):
    b=mode
    os.system("adb shell dumpsys battery > batterylevel1.txt")
    fp=open("/Users/malluri/Documents/script/batterylevel1.txt","r+")
    content=fp.readlines()
    #print(content)
    for line in content:
        if(b in line ):
            print(line)
            for j in line.split():
                #print(j)
                now = datetime.datetime.now()
                su=float((60*now.hour)+now.minute+(now.second/60))
                if(j.isdigit()):
                    print("during {0} iiiiii@@@@@@@ battery level is{1}".format(datetime.datetime.now(),j))
                    global level1
                    level2=j
                    print(level2)
                    global time2
                    time2=su
                    print(time2)
batterycheck_first("level")
batterycheck_sec("level")

def deviceno():
    str=os.system("adb get-serialno")
    return str
dev1=deviceno()
s=batterycheck_first()
print(s)
print("remove the device")
closed()
print("removed")
open()
dev2=deviceno()
while((dev1 not in dev2)):
    print("wrong device connected")
    closed() 
    open()
    dev2=deviceno()
battertcheck_sec()
discahrgelevel=level2-level1
chargelevel=leve1-level2
time=time2-time1
if(leve12>level1):
    print("discharged per {} in time {}".format(dischargelevel,time))
else:
    print("discharged per {} in time {}".format(chargelevel,time))    
        
"""

