import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinRED, GPIO.OUT)
GPIO.setup(pinD, GPIO.OUT)
GPIO.setup(pinBUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBUTTONminus, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBus, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBuss, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def get_input():

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
    