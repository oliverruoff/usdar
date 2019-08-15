import RPi.GPIO as GPIO

import detection as dt
import stepper as st

if __name__ == '__main__':
    print(dt.scan_360(4))
    st.run_stepper(512, False)
    GPIO.cleanup()
