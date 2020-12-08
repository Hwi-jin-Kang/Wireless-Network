import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

GPIO.output(18,True)
print "power_in"
time.sleep(2)

GPIO.cleanup()
