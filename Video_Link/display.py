from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1327
from PIL import ImageFont
import time
import subprocess
import os
import RPi.GPIO as GPIO
from   gpiozero import Button
import asyncio
import threading
from datetime import datetime

#Display Einrichten
serial = i2c(port=1,address=0x3D)
device = ssd1327(serial)

#

font_path = "/home/blume/Video_Link/Video_Link/arial.ttf"
            #/home/blume/Video_Link/Video_Link/arial.ttf

############################### Anzeigefunktionen und Symbole ######################################

# Zeigt akuell verbundene Gerдte an
def devices(draw):
    font_size = 15
    font = ImageFont.truetype("/home/blume/Video_Link/Video_Link/arial.ttf",font_size)
    draw.text((25,60),"no device !",font = font,fill="white")
    


# Zeigt aktuelle Uhrzeit an
def time(draw):
	
 
	# storing the current time in the variable
	c = datetime.now()

	# Displays Time
	current_time = c.strftime('%H:%M:%S')
	print('Current Time is:', current_time)
    font_size = 15
    font = ImageFont.truetype("arial.ttf",font_size)
    draw.text((40,40),"13:50",font = font,fill="white")
    

def network_rssi(draw,percent):
    x_offset = 102
    if percent > 60:
        draw.rectangle((22+x_offset,1,24+x_offset,15), outline="white",fill="white") ###############
        draw.rectangle((17+x_offset,3,19+x_offset,15), outline="white",fill="white") #############
        draw.rectangle((12+x_offset,6,14+x_offset,15), outline="white",fill="white") ###########
        draw.rectangle((7+x_offset,9,9+x_offset,15), outline="white",fill="white") #########
        draw.rectangle((2+x_offset,13,4+x_offset,15), outline="white",fill="white") ######
        
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
        
# Zeigt ein rechteck als menьfьhrung an,         
def menue_rect(draw,number): 
    draw.rectangle((0,32*number,128,32+(32*number)),outline="white", fill=None)
    return 0

def menue_sidebar(draw):
    bar_height = 12
    font_size = 12
    font = ImageFont.truetype("/home/blume/Video_Link/Video_Link/arial.ttf",font_size)
    
    draw.rectangle((0,127- bar_height,42,127),outline ="white",fill=None)
    draw.text((2,128 - bar_height),"INFO",font = font,fill="white")

    draw.rectangle((42,127 - bar_height,84,127),outline ="white",fill=None)
    draw.text((43 ,128 - bar_height),"HOME",font = font,fill="white")

    draw.rectangle((84,127 - bar_height,127,127),outline ="white",fill=None)
    draw.text((85,128 - bar_height),"SETTINGS",font = font,fill="white")
            
############################## Bildschirme und Menьfьhrung ###################################
def mainpage():
    print("Mainpage")
    with canvas(device) as draw:
        time(draw) # Zeit 
        battery(draw,95) # Batterie oben rechts 
        devices(draw) 
        network_rssi(draw,65)
        menue_sidebar(draw)
    
def infopage():
    
    with canvas(device) as draw:
        draw.text((5, 5), "IP: " + str(IP,'utf-8'), fill=255)
        draw.text((5,15),"Temp: "+str(Temp,'utf-8'), fill=255)
        rssi_short = int(str(RSSI,'utf-8')[:2])
        draw.text((5,25),"RSSI: "+str(RSSI,'utf-8')[:6], fill=255)
        draw.text((5,35),"Page"+str(page),fill=255)
    

def setting():
   # print("Settings")
    #menue_number = 1
    
    #with canvas(device) as draw:
    #   menue_rect(draw,menue_number)
        
    return 0

def user_interface():
    
    user_comando = 1
    return user_comando
    
    
