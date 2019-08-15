import RPi.GPIO as GPIO

from .detection import scan_360
from .stepper import run_stepper

if __name__ == '__main__':
    print(scan_360(4))
    run_stepper(512, False)
    GPIO.cleanup()
