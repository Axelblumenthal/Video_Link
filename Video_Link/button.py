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