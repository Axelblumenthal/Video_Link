from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1327
import time
import subprocess
import os

from   gpiozero import Button
import asyncio
import threading

import display


pinLED = 25
pinRED = 24
pinD = 23

pinBUTTON = 12
pinBUTTONminus = 16
pinBus = 20
pinBuss = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinRED, GPIO.OUT)
GPIO.setup(pinD, GPIO.OUT)
GPIO.setup(pinBUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBUTTONminus, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBus, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBuss, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


        

    



page =0
while True:
    display.mainpage()
    display.get_info(True) # print debug data on screen
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True )
    cmd = "iwconfig wlan0 | grep Quality | cut -d '=' -f2"
    RSSI = subprocess.check_output(cmd, shell = True )
    
    
    while( GPIO.input(pinBUTTON) == GPIO.HIGH):
        print("Button 4")
        page = page +1
        time.sleep(0.2)
        #mainpage()
        
        
    while( GPIO.input(pinBUTTONminus) == GPIO.HIGH):
        print("Button 3")
        page = page -1
        time.sleep(0.2),
       # infopage()
               
    while( GPIO.input(pinBus) == GPIO.HIGH):
        print("Button 2")
        page = page -1
        time.sleep(0.2),
       # infopage()
               
    while( GPIO.input(pinBuss) == GPIO.HIGH):
        print("Button 1")
        page = page -1
        time.sleep(0.2),
       # infopage()
    


    
