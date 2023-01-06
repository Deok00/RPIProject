import RPi.GPIO as gp
import time
import I2C_driver
from time import *
from Adafruit_BME280 import *
# echo 11 trig 13
# pwmpin=32
# starttime=0
# stoptime=0
# pinec=11
# pintr=13
gp.setmode(gp.BOARD)

fnd =[(1,1,0,0,0,0,0,0),
    (1,1,1,1,1,0,0,1),
    (1,0,1,0,0,1,0,0),
    (1,0,1,1,0,0,0,0),
    (1,0,0,1,1,0,0,1),
    (1,0,0,1,0,0,1,0),
    (1,0,0,0,0,0,1,0),
    (1,1,1,1,1,0,0,0),
    (1,0,0,0,0,0,0,0),
    (1,0,0,1,0,0,0,0)]
seg=[26,24,22,18,16,12,10,8]

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

degrees = sensor.read_temperature()

gp.setup(32,gp.OUT)
gp.setwarnings(False)
servo=gp.PWM(32,50)
mylcd = I2C_driver.lcd()
mylcd.lcd_clear()
gp.setmode(gp.BOARD)
gp.setup(seg,gp.OUT,initial=gp.LOW)
gp.setup(13,gp.OUT)
gp.setup(11,gp.IN)

def echo():
            
            starttime=0
            stoptime=0
            gp.output(13,0)
            sleep(1)
            gp.output(13,1)
            sleep(0.00001)
            gp.output(13,0)

            while gp.input(11)==0:
              starttime=time.time()
            while gp.input(11)==1:
              stoptime=time.time()
            time_interval=stoptime-starttime
            distance=time_interval*17000
            distance=round(distance,2)
            return distance
        
        
def servoon(angle):
            gp.setup(32,gp.OUT)
            servo.ChangeDutyCycle(angle)
            sleep(0.1)
            gp.setup(32,gp.IN)
            

def main():
            degrees = sensor.read_temperature()
            servo.start(0)
            gp.output(seg,1)
            distance=echo()
            mylcd.lcd_clear()
            mylcd.lcd_display_string(f"{distance}", 2)
            print ('Temp  = {0:0.3f} deg C'.format(degrees))
            mylcd.lcd_display_string('Temp={0:0.3f} deg C'.format(degrees),1)
            while degrees>=24:
                degrees = sensor.read_temperature()
                print ('Temp  = {0:0.3f} deg C'.format(degrees))
                mylcd.lcd_display_string('Temp={0:0.3f} deg C'.format(degrees),1)
                servoon(9)
                gp.output(seg,0)
                sleep(0.5)
                gp.output(seg,1)
                servoon(1)
                sleep(0.5)
                  
#             mylcd.lcd_display_string("door close", 1)
#             gp.cleanup()
#             mylcd.lcd_display_string("1=FND 2=servo", 1)
#             i=int(input())
#             mylcd.lcd_clear()
#             if i==1:
#                 for j in range(0,10):
#                     mylcd.lcd_display_string("0123456789",1)
#                     gp.output(seg,fnd[j])
#                     sleep(0.5)
#                      
#             if i==2:
#                      servo.start(0)
#                      mylcd.lcd_display_string("chosen 0-180",1)
#                      x=int(input())
#                      mylcd.lcd_display_string(f"{x}",2)
#                      servo.ChangeDutyCycle(x/18)
#                      sleep(0.5)
                     
            
            
            
            
            

#     if duty<maxduty:
# 		duty=0
# 		servo.ChangeDutyCycle(duty)
while True:
    main()
