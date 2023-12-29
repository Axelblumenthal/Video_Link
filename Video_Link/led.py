import RPi.GPIO as GPIO
import asyncio
import threading



pinLED = 25
pinRED = 24
pinD = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinRED, GPIO.OUT)
GPIO.setup(pinD, GPIO.OUT)

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