"""
Holds functionality for the ultra sonic sensor.
"""
import RPi.GPIO as GPIO
import time

# GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def get_reliable_distance(number_combined_measurements=5):
    measurements = [get_distance()
                    for dist in range(number_combined_measurements)]
    avg_distance = sum(measurements) / len(measurements)
    avg_deviations = [abs(avg_distance - dist) for dist in measurements]
    avg_deviation = sum(avg_deviations) / len(avg_deviations)
    filtered_distances = [measurements[i] for i in range(
        len(avg_deviations)) if avg_deviations[i] < avg_deviation]
    improved_avg_distance = sum(filtered_distances) / len(filtered_distances)
    return improved_avg_distance


def get_median_distance(number_combined_measurements=5):
    return median([get_distance() for dist
                   in range(number_combined_measurements)])


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

    return round(distance)
