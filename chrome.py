import os
#string=raw_input()
#print(type(string))
os.system("adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main")
os.system("adb shell input tap 550 770")
os.system("adb shell input tap 550 180")
string=raw_input()
os.system("adb shell input text "+string)
os.system("adb shell input keyevent 66")


