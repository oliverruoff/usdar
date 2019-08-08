import RPi.GPIO as GPIO
import math

import Stepper as st
import UltraSonic as us


def get_coord(angle, distance):
    # print('>>>sin(', angle, ') =', math.sin(angle),
     #     '*', distance, '=', math.sin(angle)*distance)
    # print('>>>cos(', angle, ') =', math.cos(angle),
     #     '*', distance, '=', math.cos(angle)*distance)
    return round(math.sin(angle)*distance), round(math.cos(angle)*distance)


def scan_360():
    env_map = []
    stepper_turn_multiplier = 2
    for i in range(256):
        angle = 360/512*i*stepper_turn_multiplier
        distance = us.get_distance()
        radians_angle = math.radians(angle)
        env_map.append(get_coord(radians_angle, distance))
        st.run_stepper(stepper_turn_multiplier, True)
    # Reset stepper position
    st.run_stepper(512, False)
    return env_map
