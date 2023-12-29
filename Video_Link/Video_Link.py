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


        
def infopage():
    with canvas(device) as draw:
        
        #GPIO.output(pinLED,GPIO.HIGH)
        time.sleep(0.1)
        draw.rectangle(device.bounding_box, outline="white",fill="black")
        #draw.rectangle((0 ,0,count,count),outline="white",fill="red")
        #draw.ellipse((64-count,64-count,64+count,64+count),outline="black",fill="white")
        #draw.ellipse((64-count,32,count,count),outline ="white",fill="black")
        draw.text((10,5),"Main Page", fill="white")
        
        draw.text((5, 5), "IP: " + str(IP,'utf-8'), fill=255)
        draw.text((5,15),"Temp: "+str(Temp,'utf-8'), fill=255)
        rssi_short = int(str(RSSI,'utf-8')[:2])
        draw.text((5,25),"RSSI: "+str(RSSI,'utf-8')[:6], fill=255)
        draw.text((5,35),"Page"+str(page),fill=255)
    

async def blink_short():
    while True:
        await asyncio.sleep(0.1)
        GPIO.output(pinLED, GPIO.HIGH)
        await asyncio.sleep(0.01)
        GPIO.output(pinLED, GPIO.LOW)
        await asyncio.sleep(0.05)
        GPIO.output(pinLED, GPIO.HIGH)
        await asyncio.sleep(0.01)
        GPIO.output(pinLED, GPIO.LOW)
        await asyncio.sleep(1)
        
async def blink_middle():
    while True:
        GPIO.output(pinLED, GPIO.HIGH)
        await asyncio.sleep(0.01)
        GPIO.output(pinLED, GPIO.LOW)
        await asyncio.sleep(0.05)
        GPIO.output(pinLED, GPIO.HIGH)
        await asyncio.sleep(0.1)
        GPIO.output(pinLED, GPIO.LOW)
        await asyncio.sleep(1.5)
        
async def blink_danger():
    while True:
        GPIO.output(pinRED, GPIO.HIGH)
        await asyncio.sleep(0.01)
        GPIO.output(pinRED, GPIO.LOW)
        await asyncio.sleep(0.05)
        GPIO.output(pinRED, GPIO.HIGH)
        await asyncio.sleep(0.01)
        GPIO.output(pinRED, GPIO.LOW)
        await asyncio.sleep(1)
        
async def blink_ok():
    while True:
        GPIO.output(pinD, GPIO.HIGH)
        await asyncio.sleep(0.1)
        GPIO.output(pinD, GPIO.LOW)
        await asyncio.sleep(0.5)
        GPIO.output(pinD, GPIO.HIGH)
        await asyncio.sleep(0.01)
        GPIO.output(pinD, GPIO.LOW)
        await asyncio.sleep(1)
        
def start_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(blink_danger(), blink_ok(),blink_short()))
    
    
    
async_thread =threading.Thread(target=start_loop)
async_thread.start()


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
    


    
