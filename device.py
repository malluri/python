
import os
import re
import sys
os.system("adb devices > devices > device.txt")
numlines = sum(1 for line in open("/Users/malluri/Documents/script/device.txt"))
print(numlines)
fp=open("/Users/malluri/Documents/script/device.txt","r+")
bf=fp.readline()
print("list",bf)
n=0
enable=re.search("List of devices attached",bf,re.I)
while enable:
    if n!=numlines-1:
        b=fp.readline()
        for i in b.split():
            print(i)
            break
        n=n+1
        #continue
    break


