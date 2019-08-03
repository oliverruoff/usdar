import RPi.GPIO as GPIO
import math

import Stepper as st
import UltraSonic as us


def get_coord(angle, distance):
    print('>>>sin(', angle, ') =', math.sin(angle),
          '*', distance, '=', math.sin(angle)*distance)
    print('>>>cos(', angle, ') =', math.cos(angle),
          '*', distance, '=', math.cos(angle)*distance)
    return round(math.sin(angle)*distance), round(math.cos(angle)*distance)


def scan_360():
    env_map = []
    stepper_turn_multiplier = 2
    for i in range(256):
        angle = 360/512*i*stepper_turn_multiplier
        distance = us.get_distance()
        print('____________________')
        print('Angle   :', angle)
        print('Distance:', distance)
        print('X       :', get_coord(angle, distance)[0])
        print('Y       :', get_coord(angle, distance)[1])
        print('____________________')
        print('angle:', angle, '/ radians(angle):', math.radians(angle))
        radians_angle = math.radians(angle)
        print('RADIANS:', radians_angle)
        env_map.append(get_coord(radians_angle, distance))
        st.run_stepper(stepper_turn_multiplier, True)
    # Reset stepper position
    st.run_stepper(512, False)
    return env_map
