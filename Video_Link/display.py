from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1327
import time
import subprocess
import os
import RPi.GPIO as GPIO
from  gpiozero import Button
import asyncio
import threading


def battery(percent):
    with canvas(device) as draw:
        draw.rectangle((2,2,15,4), outline="white",fill="black")
        draw.rectangle((16,4,17,7), outline="white",fill="black")
        

def mainpage():
    
    return 0
    

def setting():
    
    return 0
    

