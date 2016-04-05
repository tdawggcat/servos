#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

TimeToSleepAfterTRIGFalse = .5

# Steering variables
SteeringPin = 25
SteeringMaxRight = 5
SteeringMaxLeft = 9
SteeringCenter = 7

#SensorNumber = int(sys.argv[1])

GPIO.setup(SteeringPin,GPIO.OUT)
#GPIO.output(TRIG, False)
#time.sleep(TimeToSleepAfterTRIGFalse)

pwm=GPIO.PWM(SteeringPin,50)
print "Centering"
pwm.start(SteeringCenter)
print "Sleeping 2 seconds"
time.sleep(2)
print "Right"
pwm.ChangeDutyCycle(SteeringMaxRight)
print "Sleeping 2 seconds"
time.sleep(2)
print "Left"
pwm.ChangeDutyCycle(SteeringMaxLeft)
print "Sleeping 2 seconds"
time.sleep(2)
print "Centering"
pwm.ChangeDutyCycle(SteeringCenter)
print "Sleeping 2 seconds"
time.sleep(2)
print "Stopping Pulse Width Modulation"
pwm.stop()

print "Cleaning up GPIO"
GPIO.cleanup()

