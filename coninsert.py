import os
import time
def contact_insert():
       f=open("/Users/malluri/Documents/script/insercnt.txt","r+")
       
       b=f.read().splitlines()
       print (b)
       for i in range(0,len(b),2):
           print (i)
           st="adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name " + b[i] + " -e phone " +b[i+1]
           os.system(st)
           os.system("adb shell input tap 1079 148")
           os.system("adb shell input keyevent 4")
           time.sleep(2)
           

contact_insert()
