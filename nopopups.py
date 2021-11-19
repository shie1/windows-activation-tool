from time import sleep
from os import system
from threading import Thread
from sys import exit

stop_flag = True

def stop():
    global stop_flag
    stop_flag = False

def __main():
    global stop_flag
    while stop_flag:
        try: system("taskkill /f /im wscript.exe >nul 2>&1")
        except: pass
        sleep(.25)
    exit()
        
Thread(target=__main).start()
