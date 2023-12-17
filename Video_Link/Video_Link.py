from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1327
import time
import subprocess
import os
import RPi.GPIO as GPIO
import asyncio
import threading
pinLED = 25
pinBUTTON = 20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinBUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# das ist ein test für ein Update
# das ist ein weiter test für ein update

serial = i2c(port=1,address=0x3D)
device = ssd1327(serial)
count =0

async def blink_short():
    while True:
        GPIO.output(pinLED, GPIO.HIGH)
        await asyncio.sleep(1)
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
        
def start_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(blink_short())
    
    
    
async_thread =threading.Thread(target=start_loop)
async_thread.start()



while True:
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True )
    cmd = "iwconfig wlan0 | grep Quality | cut -d '=' -f2"
    RSSI = subprocess.check_output(cmd, shell = True )
    curr_gp_times =os.times()
    
  
    
    with canvas(device) as draw:
        
        #GPIO.output(pinLED,GPIO.HIGH)
        time.sleep(1)
        draw.rectangle(device.bounding_box, outline="white",fill="black")
       # draw.rectangle((0 ,0,count,count),outline="white",fill="red")
        #draw.ellipse((64-count,64-count,64+count,64+count),outline="black",fill="white")
        #draw.ellipse((64-count,32,count,count),outline ="white",fill="black")
        #draw.text((10,40),"Hello Wordl"+ str(count), fill="white")
        draw.text((5, 5), "IP: " + str(IP,'utf-8'), fill=255)
        draw.text((5,15),"Temp: "+str(Temp,'utf-8'), fill=255)
        rssi_short = int(str(RSSI,'utf-8')[:2])
        draw.text((5,25),"RSSI: "+str(RSSI,'utf-8')[:6], fill=255)
        
        
        if pinBUTTON == GPIO.HIGH:
            print("Button test")

    
