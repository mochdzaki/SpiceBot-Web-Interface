import Jetson.GPIO as GPIO
import time

# Pin Definitions
servo_pin = 33  # Pin where the signal wire of the servo is connected

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM on the servo pin at 50Hz
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

try:
    while True:
        # Move the servo to 90 degrees (adjust the duty cycle for angle)
        pwm.ChangeDutyCycle(7.5)  # 7.5 is approx 90 degrees
        time.sleep(1)

        # Move the servo to 0 degrees
        pwm.ChangeDutyCycle(2.5)  # 2.5 is approx 0 degrees
        time.sleep(1)

        # Move the servo to 180 degrees
        pwm.ChangeDutyCycle(12.5)  # 12.5 is approx 180 degrees
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
