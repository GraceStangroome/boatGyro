# This is the main module that connects the Stepper Motor code and the MEMS sensor code together. It is coded to be controlled by a GUI. It also amanages a save file system using a database.
# It includes the calculations that control the motor based on output from the accelerometer
# You will require the other three modules to run this module called "sensor1.py", "led.py" and "motor_code1.py" within the same file.
# The code is designed to be run on a Raspberry Pi, and cannot run on another device unless to change "RPi" in the other modules

import motor_code2 as motor
import sensor1 as sensor
import led
import RPi.GPIO as GPIO
import DataLog as log
from time import sleep
global r  # So that the variable quit can stop the program
 
def run():
    r = 0   # To ensure it will loop
    x_angle = sensor.get_x_rotation()
    log.current("The x angle is {}".format(x_angle))
    try:
        while r == 0:
            x_angle = sensor.get_x_rotation()
            if x_angle < 0:
                log.current("the x angle is {}".format(x_angle))
                motor.run_motor(direction="clockwise")
                led.on()
                sleep(0.5)
                led.off()
            elif x_angle > 0:
                log.current("the x angle is {}".format(x_angle))
                motor.run_motor(direction="anti")
                led.on()
                sleep(0.5)
                led.off()
            else:
                log.current("the x angle is {}".format(x_angle))
                led.on()
                sleep(0.5)
                led.off()
        log.records("program loop ran successfully.")
    except Exception as error:
        log.records("program loop stopped because of {}.".format(error))


def quit():
    r = 1   # as r is what controls the loop in the run variable
    # To quit properly
    motor.stop_motor()    
    led.off
    log.records("program stopped by user")
