 import os
 a=str(input("TERMUX-API APP INSTALLED Y/N "))
if a=="n":
    os.system("termux-open --view https://play.google.com/store/
apps/details?id=com.termux.api")
if a=="y":
    print("good boy")
os.system("pkg install termux-api -y")
os.system("cd /data/data/com.termux/files/home/andro_informer")
os.system(" python ai.py")

