
import time
import os
import subprocess
class Airplane:


    def checkairplanemode(self):
        #checking airplane mode whether  it is on
        sp = subprocess.Popen("adb shell settings get global airplane_mode_on",stdout=subprocess.PIPE,shell=True)
        #if it is on above code returns 1
        (output,err)= sp.communicate()
        print(str(output.decode()))
        string1=str(output.decode())
        if "1" in string1:
            return True
        else:
            return False

    def aiplane_toggle(self):
        #if airplane mode is on , below code maakes turnoff
        ad = subprocess.Popen("adb shell settings put global airplane_mode_on 0", stdout = subprocess.PIPE, shell=True)
        (output, err) = ad.communicate()


    def sim_status(self):
        bf = subprocess.Popen("adb shell getprop ",stdout=subprocess.PIPE,shell=True)
        (output, err) = bf.communicate()
        #print(str(output.decode()))
        string = str((output.decode()))
        #print(string)
        fp = str(string).splitlines()
        #print(fp)
        if "[gsm.sim.state]: [NOT_READY,[NOT_READY]" in fp:
            return False
        else:
            print("sim is ready")
            return True

    def call(self):
        f = open("/Users/malluri/Documents/script/connum.txt", "r+")
        buff = f.read()
        for i in buff.split():
            print(i)
            fp=subprocess.Popen("adb shell am start -a android.intent.action.CALL -d tel:" + i,stdout=subprocess.PIPE,shell=True)
            (output, err) = fp.communicate()
            time.sleep(5)
            f=subprocess.Popen("adb shell input keyevent KEYCODE_ENDCALL",stdout=subprocess.PIPE,shell=True)
            (out, err) = f.communicate()

    def sms(self):
        f = open("/Users/malluri/Documents/script/connum.txt", "r+")
        buff = f.read()
        #   texte="this is manoj"
        for i in buff.split():
            print(i)
            #       os.system("adb shell am start -a android.intent.action.SENDTO -d sms:9505895588"" --es sms_body ""this is manoj"" --ez exit_on_sent true"
            s1 = subprocess.Popen("adb shell am start -a android.intent.action.SENDTO -d sms:" + i,stdout=subprocess.PIPE,shell=True)
            (output, err) = s1.communicate()
            s2 = subprocess.Popen("adb shell input text thisismanoj ", stdout=subprocess.PIPE, shell=True)
            (op, err) = s2.communicate()
            s3 = subprocess.Popen("adb shell input tap 980 910 ", stdout=subprocess.PIPE, shell=True)
            (out, err) = s3.communicate()
            time.sleep(5)
            os.system("adb shell input keyevent 4")
    def total(self):
        state = self.checkairplanemode(Airplane)
        print(state)
        if state:
            self.aiplane_toggle(Airplane)
        time.sleep(2)
        simstate = self.sim_status(Airplane)
        print(simstate)
        if simstate:
            print("sim is ready ")
            self.call(Airplane)







