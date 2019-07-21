import RPi.GPIO as GPIO
import math

import Stepper as st
import UltraSonic as us

def get_coord(angle, distance):
    return math.sin(angle)*distance, math.cos(angle)*distance

def scan_360():
    env_map = scan_range(360, True)
    # move stepper back to initial position
    st.turn_stepper_angle(360, False)
    return env_map

def scan_range(degree, clockwise=True):
    env_map = []
    for angle in range(degree):
        print('Angle:', angle)
        distance = us.get_distance()
        print('Distance:', distance)
        env_map.append(get_coord(angle, distance))
        st.turn_stepper_angle(1, clockwise)
    return env_map