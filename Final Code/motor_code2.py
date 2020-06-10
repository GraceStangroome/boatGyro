# This code is sourced from the schematics of the 28BYJ-48 Stepper Motors sold with ULN2003 drivers by Elegoo.
# The schematics can be found here: http://domoticx.com/raspberry-pi-stappenmotor-28byj-48-via-gpio/
# !/bin/python
import RPi.GPIO as GPIO
import DataLog as log
# importing the time library for time functions.
from time import sleep
# Set the pin mode to Broadcom SOC.


def run_motor(direction="clockwise"):
    GPIO.setmode(GPIO.BCM)
    # Turn off warnings.
    GPIO.setwarnings(False)
    # Set the GPIO pins for the stepper motor:
    StepPins = [17,18,14,15]
    for pin in StepPins:
        log.current("setting up pin {}".format(pin))
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)
    log.records("pins set up.")

    # Define variables.
    StepCounter = 0
    LoopCounter = 0
    # Dictionary used to translate speed value into a delay that is used in the stepper motor sequence.
    # Here speed could be set to 1, 2, 3 or 4
    # speed_delay_settings = {1:10000, 2:5000, 3:2000}
    # delay = speed_delay_settings[speed]

    
    # Define simple order
    StepCount1 = 4
    
    # for anticlockwise
    Seq1 = [0,1,2,3]
    Seq1[0] = [1,0,0,0]
    Seq1[1] = [0,1,0,0]
    Seq1[2] = [0,0,1,0]
    Seq1[3] = [0,0,0,1]

    #for clockwise
    Seq = [3,2,1,0]     # blank array of correct dimension. 
    Seq[0] = [0,0,0,1]
    Seq[1] = [0,0,1,0]
    Seq[2] = [0,1,0,0]
    Seq[3] = [1,0,0,0]
    
    
    StepCount = StepCount1
    
    if direction == "clockwise":
        i = 0
        while i < 200:
            for pin in [3,2,1,0]:
                xpin = StepPins[pin]
                if Seq[StepCounter][pin]!=0:
                    log.current("step: {} gpio active: {}".format(StepCounter,xpin))
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

                StepCounter += 1
                i = i + 1

    # When we arrive at the end of the sequence, start again
                if StepCounter == StepCount:
                  StepCounter = 0
                if StepCounter<0:
                  StepCounter = StepCount

    #  Wait for the next step (lower = faster rotation speed)
                sleep(0.01)
                GPIO.output(xpin, False)
                LoopCounter = LoopCounter + 1
        log.records("motor turned clockwise")
    else:
        i = 0
        while i < 200:
            for pin in [0,1,2,3]:
                xpin = StepPins[pin]
                if Seq1[StepCounter][pin]!=0:
                    log.current("step: {} gpio active: {}".format(StepCounter,xpin))
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

                StepCounter += 1
                i = i + 1

    # When we arrive at the end of the sequence, start again
                if StepCounter == StepCount:
                  StepCounter = 0
                if StepCounter<0:
                  StepCounter = StepCount

    #  Wait for the next step (lower = faster rotation speed)
                sleep(0.01)
                GPIO.output(xpin, False)
                LoopCounter = LoopCounter - 1
        log.records("motor turned anticlockwise")
        
    
    
def stop_motor():
    # Turn off warnings.
    GPIO.setwarnings(False)
    # Set the GPIO pins for the stepper motor:
    StepPins = [17,18,14,15]
    for pin in StepPins:
        log.records("setting down pin {}".format(pin))
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)
    GPIO.cleanup()
    log.records("cleaned gpio pins for motor")