import os
i="9121854800"
texte="this is manoj"
os.system("adb shell am start -a android.intent.action.SENDTO -d sms:"+i+" --es sms_body ""+texte+"" --ez exit_on_sent true")
os.system("adb shell input keyevent 22") 
os.system("adb shell input keyevent 66")
