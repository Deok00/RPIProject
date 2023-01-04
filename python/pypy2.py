import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
LED1=8
LED2=10
LED3=12
GPIO.setup(LED2,GPIO.OUT,intial=GPIO.LOW)
GPIO.output(LED2,GPIO.HIGH)
time.sleep(5)