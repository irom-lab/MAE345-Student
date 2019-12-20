group_number = 3

# Code adapted from: https://github.com/bitcraze/crazyflie-lib-python/blob/master/examples/autonomousSequence.py

import time
# CrazyFlie imports:
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.positioning.position_hl_commander import PositionHlCommander
import numpy as np
import cv2




## Some helper functions:
## -----------------------------------------------------------------------------------------

# Ascend and hover:
def set_PID_controller(cf):
    # Set the PID Controller:
    print('Initializing PID Controller')
    cf.param.set_value('stabilizer.controller', '1')
    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')
    time.sleep(2)
    return

# Ascend and hover:
def ascend_and_hover(cf):
    print('Ascending to hover:')
    # Ascend:
    for y in range(10):
        cf.commander.send_hover_setpoint(0, 0, 0, y / 25)
        time.sleep(0.1)
    # Hover at 0.5 meters:
    for _ in range(30):
        cf.commander.send_hover_setpoint(0, 0, 0, 0.5)
        time.sleep(0.1)
    return

# Follow the setpoint sequence trajectory:
def run_position(cf, position):

    print('Setting position {}'.format(position))
    for i in range(10):
        cf.commander.send_position_setpoint(position[0],
                                            position[1],
                                            position[2],
                                            position[3])
        time.sleep(0.1)

def findGreatesContour(contours):
    largest_area = 0
    largest_contour_index = -1
    i = 0
    total_contours = len(contours)

    while i < total_contours:
        area = cv2.contourArea(contours[i])
        if area > largest_area:
            largest_area = area
            largest_contour_index = i
        i += 1

    #print(largest_area)

    return largest_area, largest_contour_index


def check_contours(frame):

    print('Checking image:')

    # These define the upper and lower HSV for the red obstacles
    # May change on different drones.
    lb = (145, 3, 250)
    ub = (155, 40, 255)

    # Do the contour detection on the input frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Compute 
    mask = cv2.inRange(hsv, lb, ub)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    largest_area, largest_contour_index = findGreatesContour(contours)

    print(largest_area)

    if largest_area > 100:
        return True
    else:
        return False


# Follow the setpoint sequence trajectory:
def adjust_position(cf, current_y):

    print('Adjusting position')

    steps_per_meter = int(10)
    for i in range(steps_per_meter):
        current_y = current_y - 1.0/float(steps_per_meter)
        position = [0, current_y, 0.5, 0.0]

        print('Setting position {}'.format(position))
        for i in range(10):
            cf.commander.send_position_setpoint(position[0],
                                                position[1],
                                                position[2],
                                                position[3])
            time.sleep(0.1)

    cf.commander.send_stop_setpoint()
    # Make sure that the last packet leaves before the link is closed
    # since the message queue is not flushed before closing
    time.sleep(0.1)
    return current_y


# Hover, descend, and stop all motion:
def hover_and_descend(cf):
    print('Descending:')
    # Hover at 0.5 meters:
    for _ in range(30):
        cf.commander.send_hover_setpoint(0, 0, 0, 0.5)
        time.sleep(0.1)
    # Descend:
    for y in range(10):
        cf.commander.send_hover_setpoint(0, 0, 0, (10 - y) / 25)
        time.sleep(0.1)
    # Stop all motion:
    for i in range(10):
        cf.commander.send_stop_setpoint()
        time.sleep(0.1)
    return

## -----------------------------------------------------------------------------------------

## The following code is the main logic that is executed when this script is run

## -----------------------------------------------------------------------------------------

# Set the URI the Crazyflie will connect to
uri = f'radio://0/{group_number}/2M'

# Initialize all the CrazyFlie drivers:
cflib.crtp.init_drivers(enable_debug_driver=False)

# Scan for Crazyflies in range of the antenna:
print('Scanning interfaces for Crazyflies...')
available = cflib.crtp.scan_interfaces()
# List local CrazyFlie devices:
print('Crazyflies found:')
for i in available:
    print(i[0])

# Check that CrazyFlie devices are available:
if len(available) == 0:
    print('No Crazyflies found, cannot run example')
else:
    ## Ascent to hover; run the sequence; then descend from hover:
    # Use the CrazyFlie corresponding to team number:
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        # Get the Crazyflie class instance:
        cf = scf.cf
        current_y = 0.0

        # Initialize and ascend:
        t = time.time()
        elapsed = time.time() - t
        ascended_bool = 0

        cap = cv2.VideoCapture(0)
        while(cap.isOpened()):

            ret, frame = cap.read()

            elapsed = time.time() - t
            if(elapsed > 5.0):

                print('Capturing.....')

                if ret==True:
                    #cv2.imshow('frame',frame)

                    if(ascended_bool==0):
                        set_PID_controller(cf)
                        ascend_and_hover(cf)
                        ascended_bool = 1
                    else:

                        if(check_contours(frame)):
                            current_y = adjust_position(cf, current_y)

            if(elapsed > 10.0):
                        break

        cap.release()

        # Descend and stop all motion:
        hover_and_descend(cf)

print('Done!')
return
