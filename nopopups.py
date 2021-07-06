from time import sleep
from os import system
from threading import Thread
from sys import exit

i = True

def stop():
    global i
    i = False

def __main():
    global i
    while i == True:
        try: system("taskkill /f /im wscript.exe >nul 2>&1")
        except: ""
        sleep(.25)
    exit()
        
Thread(target=__main).start()