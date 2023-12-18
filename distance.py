import RPi.GPIO as GPIO
import time

VoltageIn = 18


GPIO.setmode(GPIO.BCM)

GPIO.setup(VoltageIn, GPIO.IN)

while True:
	Vin = GPIO.input(VoltageIn)
	print(Vin)
	print("!")
	if(Vin == 1):
		print("Empty the trash bin")
	
	time.sleep(1)
