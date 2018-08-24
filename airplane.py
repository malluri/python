import os
import re
import sys
import time
def checkairplanemode():
    mode=0
    os.system("adb shell getprop > plane.txt")
    fp=open("/Users/malluri/Documents/script/plane.txt","r+")
    buf="[init.svc.p2p_supplicant]: [stopped]"
    while 1:
        bf=fp.readline()
        if(buf in bf):
            mode=1  
            break
    if mode:
        return(True)
    else:
        return(False)
mode=checkairplanemode()
print(mode)
def aiplane_toggle():
           os.system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
           os.system("adb shell settings put global airplane_mode_on 0")
 #          os.system("adb shell input keyevent 4")
           
def sim_status():
    flag=0
    os.system("adb shell getprop > plane.txt")
    f=open("/Users/malluri/Documents/script/plane.txt","r+")
    sim="[gsm.sim.state]: [READY,READY]"
    sim1="[gsm.sim.state]: [READY,NOT_READY]"
    sim2="[gsm.sim.state]: [NOT_READY,READY]"
    sim3="[gsm.sim.state]: [NOT_READY,[NOT_READY]"
    while 1:
        bs=f.readline()
        if(sim in bs or sim1 in bs or sim in bs ):
            flag=1
           # print(flag)
            break
    if flag:
        return(True)
    else:
        return(False)
status=sim_status()
#print(status)

if mode:
    aiplane_toggle()
    time.sleep(1)
    print("check sim status")
    sim_status()
if status:
    print("sim is in ready state")
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
    
   
def call():
    f=open("/Users/malluri/Documents/script/connum.txt","r+")
    buff=f.read()
    for i in buff.split():
        print(i)
        os.system("adb shell am start -a android.intent.action.CALL -d tel:"+i)
        time.sleep(10)
        os.system("adb shell input keyevent KEYCODE_ENDCALL")
    
call()

def sms():
    f=open("/Users/malluri/Documents/script/connum.txt","r+")
    buff=f.read()
 #   texte="this is manoj"
    for i in buff.split():
        print(i)
 #       os.system("adb shell am start -a android.intent.action.SENDTO -d sms:9505895588"" --es sms_body ""this is manoj"" --ez exit_on_sent true"
        os.system("adb shell am start -a android.intent.action.SENDTO -d sms:"+i)
        os.system("adb shell input text thisismanoj")
        os.system("adb shell input tap 980 910")
  
        time.sleep(5)
        os.system("adb shell input keyevent 4")
        
sms()

   
