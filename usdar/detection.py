import RPi.GPIO as GPIO
import math

import stepper as st
import ultrasonic as us


def get_coord(angle, distance, log=False):
    if log:
        print('>>>sin(', angle, ') =', math.sin(angle),
              '*', distance, '=', math.sin(angle)*distance)
        print('>>>cos(', angle, ') =', math.cos(angle),
              '*', distance, '=', math.cos(angle)*distance)
    return round(math.sin(angle)*distance), round(math.cos(angle)*distance)


def scan_360(stepper_turn_multiplier=2):
    env_map = []
    for i in range(int(512/stepper_turn_multiplier)):
        angle = 360/512*i*stepper_turn_multiplier
        distance = us.get_distance()
        radians_angle = math.radians(angle)
        env_map.append(get_coord(radians_angle, distance))
        st.run_stepper(stepper_turn_multiplier, True)
    return env_map
