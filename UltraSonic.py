"""
Holds functionality for the ultra sonic sensor.
"""
import RPi.GPIO as GPIO
import time

# GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 20
GPIO_ECHO = 21

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def get_distance():
    """Triggers the ultra sonic sensor and measures the distance.

    Returns:
        float -- Distance measured.
    """
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    # multiplay with speed of sound (34300 cm/s)
    # divide by 2 (since double distance)
    distance = (time_elapsed * 34300) / 2

    return distance


print('Distance:', get_distance(), 'cm')
GPIO.cleanup()
