"""
Holds functionality to move the stepper motor.
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
STEPPER_PINS = [21, 20, 16, 12]

for pin in STEPPER_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

HALFSTEP_SEQ = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]


def run_stepper(steps, clockwise=True):
    """Runs the stepper motor for the given number of steps.
       Note, that "clockwise" depends on pin setup.
       512 steps == 1 round.
    Arguments:
        steps {int} -- Number of steps the motor will do.

    Keyword Arguments:
        clockwise {boolean} -- Tells if the motor runs clockwise or counter clockwise. (default: {True})
    """
    halfstep_range = range(8) if not clockwise else list(reversed(range(8)))
    for i in range(steps):
        for halfstep in halfstep_range:
            for pin in range(4):
                GPIO.output(STEPPER_PINS[pin], HALFSTEP_SEQ[halfstep][pin])
            time.sleep(0.001)

def turn_stepper_angle(angle_in_degree, clockwise=True):
    run_stepper(int(512/360 * angle_in_degree), clockwise)

