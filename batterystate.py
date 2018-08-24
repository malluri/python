import re
import os
import time
def batterystatus(state):
    b=state
    os.system("adb shell dumpsys battery > battery.txt")
    fp=open("/Users/malluri/Documents/script/battery.txt","r+")
    content=fp.readlines()
    #print(content)
    for line in content:
        print(line)
        if b in line :
            #print(line)
            for j in line.split():
                #print(j)
                t = time.localtime()
                if(j.isdigit()):
                    print("At {0}  battery level is : {1}".format(time.asctime(t),j))
str=raw_input("enter battery service state")
batterystatus(str)
