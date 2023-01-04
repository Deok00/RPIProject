import RPi.GPIO as gp

import time

led= [12,32,33]

gp.setwarnings(False)

gp.setmode(gp.BOARD)

gp.setup(led,gp.OUT,initial=gp.LOW)

pwm_led1=gp.PWM(led[0],500)
pwm_led2=gp.PWM(led[1],500)
pwm_led3=gp.PWM(led[2],500)

pwm_led1.start(0)
pwm_led2.start(0)
pwm_led3.start(0)

try:
    for i in range(101):
        pwm_led1.ChangeDutyCycle(i)
        pwm_led2.ChangeDutyCycle(i)
        pwm_led3.ChangeDutyCycle(i)
        time.sleep(0.1)
        
    for i in range(100,1,-1):
        pwm_led1.ChangeDutyCycle(i)
        pwm_led2.ChangeDutyCycle(i)
        pwm_led3.ChangeDutyCycle(i)
        time.sleep(0.1)
        
finally:
    pwm_led.stop()
    gp.cleanup()