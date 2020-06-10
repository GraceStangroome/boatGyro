# This code turns an LED on/off using pin 23.
import RPi.GPIO as GPIO
import time
import DataLog as log

# Turning the LED on 
def on():
    pin_ = 23
# Setting up GPIO's
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin_,GPIO.OUT)
    log.current("light on")
    GPIO.output(pin_, GPIO.HIGH)
    time.sleep(0.025)

# Turning the LED off
def off():
    pin_ = 23
# Setting up GPIO's
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin_,GPIO.OUT)
    log.current("light off")
    GPIO.output(pin_, GPIO.LOW)
# CLosing the GPIO neatly
    GPIO.cleanup()