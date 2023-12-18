import RPi.GPIO as GPIO
import time

magnet1 = 26
magnet2 = 6
magnet3 = 13
magnet4 = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(magnet1, GPIO.IN)
GPIO.setup(magnet2, GPIO.IN)
GPIO.setup(magnet3, GPIO.IN)
GPIO.setup(magnet4, GPIO.IN)


def BinsAttachementStatusUpdate():
    status = {"black": (GPIO.input(magnet1) == 1),
              "blue": (GPIO.input(magnet2) == 1),
              "orange": (GPIO.input(magnet3) == 1),
              "green": (GPIO.input(magnet4) == 1)
              }
    return status
