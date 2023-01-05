import RPi.GPIO as gp

import time

gp.setwarnings(False)
gp.setmode(gp.BOARD)
seg=[26,24,22,18,16,12,10,8]
gp.setup(seg,gp.OUT,initial=gp.LOW)

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



while True:
    try:
         i=int(input())
         gp.output(seg,fnd[i])
         
    except:
        pass
