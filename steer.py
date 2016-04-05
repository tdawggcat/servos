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

SteeringDegree = int(sys.argv[1])
SteeringDegreeFactor = 1./45.
SteeringDegreeFactorAdd = 5

SteeringDutyCycle = (SteeringDegreeFactor * SteeringDegree) + SteeringDegreeFactorAdd

#print "SteeringDegreeFactor:",SteeringDegreeFactor
#print "SteeringDegree:",SteeringDegree
#print "SteeringDegreeFactorAdd:",SteeringDegreeFactorAdd
#print "SteeringDutyCycle:",SteeringDutyCycle


GPIO.setup(SteeringPin,GPIO.OUT)
#GPIO.output(TRIG, False)
#time.sleep(TimeToSleepAfterTRIGFalse)

pwm=GPIO.PWM(SteeringPin,50)
#pwm.start(SteeringCenter)
#time.sleep(2)
pwm.start(SteeringDutyCycle)
time.sleep(.1)
pwm.stop()

GPIO.cleanup()

