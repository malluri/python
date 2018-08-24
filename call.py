import os
import time
def call():
    num=(raw_input())
    print("adb shell am start -a android.intent.action.CALL -d tel: "+num)
    time.sleep(1)
    os.system("adb shell am start -a android.intent.action.CALL -d tel:"+num)

