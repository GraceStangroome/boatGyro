# This code originates from the Raspberrry Pi Project https://tutorials-raspberrypi.com/measuring-rotation-and-acceleration-raspberry-pi/
# It has been edited by Grace Stangroome to use English based variables and comments.
#!/usr/bin/python
import smbus
import math
import DataLog as log
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
 
def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

# vector add of y and z
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z)) # atan2 just means inverse tan
    return -math.degrees(radians)
 
def get_x_rotation_angle(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
 
bus = smbus.SMBus(1) # bus = smbus.SMBus(0)
address = 0x68       # via i2cdetect
 
try:
    # Activate to be able to address the module
    bus.write_byte_data(address, power_mgmt_1, 0)

    gyroskop_xout = read_word_2c(0x43)
    gyroskop_yout = read_word_2c(0x45)
    gyroskop_zout = read_word_2c(0x47)
     
    log.current("gyroscope x axis: {}, scale: {}".format(gyroskop_xout, (gyroskop_xout / 131)))
    log.current("gyroscope y axis: {}, scale: {}".format(gyroskop_yout, (gyroskop_yout / 131)))
    log.current("gyroscope z axis: {}, scale: {}".format(gyroskop_zout, (gyroskop_zout / 131)))
    
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)
     
    accel_xout_scale = accel_xout / 16384.0
    accel_yout_scale = accel_yout / 16384.0
    accel_zout_scale = accel_zout / 16384.0

    log.current("acceleration on x: {}, scale: {}".format(accel_xout, accel_xout_scale))
    log.current("acceleration on y: {}, scale: {}".format(accel_yout, accel_yout_scale))
    log.current("acceleration on z: {} scale: {}".format(accel_zout, accel_zout_scale))
    
    log.records("gyroscope and accelerometer read.")
except Exception as error:
    log.records("error occured: {}".format(error))

def get_x_rotation():
    # read values from accelerometer again - needed to be called properly in the main file
    try:
        accel_xout = read_word_2c(0x3b)
        accel_yout = read_word_2c(0x3d)
        accel_zout = read_word_2c(0x3f)
        angle = get_x_rotation_angle(accel_xout, accel_yout, accel_zout)
        # So that it won't move when flat
        rounded_rotation = round(angle)
    # return theta after having done the maths
        return rounded_rotation
        log.records("angle fetched")
    except Exception as error:
        log.records("error occured: {}".format(error))
