from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1327
from PIL import ImageFont
import time
import subprocess
import os
import RPi.GPIO as GPIO
from  gpiozero import Button
import asyncio
import threading


#Display Einrichten
serial = i2c(port=1,address=0x3D)
device = ssd1327(serial)


############################### Anzeigefunktionen und Symbole ######################################

# Zeigt akuell verbundene Geräte an
def devices(draw):
    font_size = 15
    font = ImageFont.truetype("/Video_Link/data/arial.ttf",font_size)
    draw.text((10,60),"no device !",font = font,fill="white")
    


# Zeigt aktuelle Uhrzeit an
def time(draw):
    font_size = 15
    #arial_font = ImageFont.load_default(         )
    font = ImageFont.truetype("/home/blume/Desktop/arial.ttf",font_size)
    draw.text((10,40),"13:50",font = font,fill="white")
    

def network_rssi(draw,percent):
    if percent > 60:
        draw.rectangle((22,1,24,15), outline="white",fill="white") ###############
        draw.rectangle((17,3,19,15), outline="white",fill="white") #############
        draw.rectangle((12,6,14,15), outline="white",fill="white") ###########
        draw.rectangle((7,9,9,15), outline="white",fill="white") #########
        draw.rectangle((2,13,4,15), outline="white",fill="white") ######
        
    return 0

# Zeigt Battery symbol an mit 3 balken an 
def battery(draw,percent): #TODO Bei unter 20% Blinken
    draw.rectangle((2,2,40,15), outline="white",fill="black")
    draw.rectangle((40,3,42,13), outline="white",fill="black")
    
    if percent > 80:
        
        draw.rectangle((29,4,38,13), outline="white",fill="white")
        draw.rectangle((16,4,26,13), outline="white",fill="white")
        draw.rectangle((4,4,13,13), outline="white",fill="white")
           
    if percent <= 60 and percent >= 41:
        
        draw.rectangle((16,4,26,13), outline="white",fill="white")
        draw.rectangle((4,4,13,13), outline="white",fill="white")
            
    if percent <= 40 and percent >= 20:
        print("Low Battery !")
        draw.rectangle((4,4,13,13), outline="white",fill="white")    
        
# Zeigt ein rechteck als menüführung an,         
def menue_rect(draw,number): 
    draw.rectangle((0,32*number,128,32+(32*number)),outline="white", fill=None)
    return 0
    
            
############################## Bildschirme und Menüführung ###################################
def mainpage():
    print("Mainpage")
    with canvas(device) as draw:
        time(draw) # Zeit 
        battery(draw,95) # Batterie oben rechts 
        devices(draw) 
        # Netzqualtität
     
    

def setting():
    print("Settings")
    menue_number = 1
    
    with canvas(device) as draw:
        menue_rect(draw,menue_number)
        
    return 0

def user_interface():
    
    user_comando = 1
    return user_comando
    
    
