"""
Holds functionality to move the stepper motor.
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
STEPPER_PINS = [6, 13, 19, 26]

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


def run_stepper(steps, forward=True):
    """Runs the stepper motor for the given number of steps.

    Arguments:
        steps {int} -- Number of steps the motor will do.

    Keyword Arguments:
        forward {boolean} -- Tells if the motor runs forward or backward. (default: {True})
    """
    halfstep_range = range(8) if forward else list(reversed(range(8)))
    for i in range(steps):
        for halfstep in halfstep_range:
            for pin in range(4):
                GPIO.output(STEPPER_PINS[pin], HALFSTEP_SEQ[halfstep][pin])
            time.sleep(0.001)


run_stepper(512)  # 512 steps == 1 round -> forward
run_stepper(512, False)  # -> backward

GPIO.cleanup()
