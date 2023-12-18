import RPi.GPIO as GPIO
VoltageIn = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(VoltageIn, GPIO.IN)


def trashDetected():
    Vin = GPIO.input(VoltageIn)
    print(Vin)

    if (Vin == 1):
        print("Trash Detected")
        return True

    return False
