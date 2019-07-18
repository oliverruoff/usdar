import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
stepper_pins = [6, 13, 19, 26]

for pin in stepper_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

halfstep_seq = [
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
    halfstep_range = range(8) if forward else list(reversed(range(8)))
    for i in range(steps):
        for halfstep in halfstep_range:
            for pin in range(4):
                GPIO.output(stepper_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)


run_stepper(512)  # 512 steps == 1 round -> forward
run_stepper(512, False)  # -> backward

GPIO.cleanup()
