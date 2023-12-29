import RPi.GPIO as GPIO

pinBUTTON = 12
pinBUTTONminus = 16
pinBus = 20
pinBuss = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(pinBUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBUTTONminus, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBus, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinBuss, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def get_input():
    page =0
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
    