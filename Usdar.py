import RPi.GPIO as GPIO
import math

import Stepper as st
import UltraSonic as us

def get_coord(angle, distance):
    #print('>>>sin(', angle, '=', math.sin(angle), '*', distance, '=',math.sin(angle)*distance )
    #print('>>>cos(', angle, '=', math.cos(angle), '*', distance, '=',math.cos(angle)*distance )
    return math.sin(angle)*distance, math.cos(angle)*distance


def scan_360():
    env_map = []
    stepper_turn_multiplier = 2
    for i in range (256):
        angle = 360/512*i*stepper_turn_multiplier
        distance = us.get_reliable_distance()
        #print('____________________')
        #print('Angle   :', angle)
        #print('Distance:', distance)
        #print('X       :', get_coord(angle, distance)[0])
        #print('Y       :', get_coord(angle, distance)[1])
        #print('____________________')
        env_map.append(get_coord(math.radians(angle), distance))
        st.run_stepper(stepper_turn_multiplier, True)
    # Reset stepper position
    st.run_stepper(512, False)
    return env_map