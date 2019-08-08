import RPi.GPIO as GPIO

import Usdar as usdar

print(usdar.scan_360())


GPIO.cleanup()