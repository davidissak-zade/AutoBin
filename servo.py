import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
servo_pwm = GPIO.PWM(5, 50)


def activateServo():
    servo_pwm = setup_servo()
    servo_pwm.start(0)
    time.sleep(1)

    servo_pwm.ChangeDutyCycle(12)
    time.sleep(1)
    time.sleep(3)
    servo_pwm.ChangeDutyCycle(2)
    time.sleep(1)

    servo_pwm.stop()
    GPIO.cleanup()
