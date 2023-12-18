from time import sleep
import RPi.GPIO as GPIO
import keyboard

DIR = 23 # Direction GPIO Pin
STEP = 24  # Step GPIO Pin
CW = 1 # Clockwise Rotation (1)
CCW = 0 # Counterclockwise Rotation (0)

AnglePerStep = 1.8


GPIO.setmode(GPIO.BCM	)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

def SetCWDirection():
	GPIO.output(DIR, CW)	

def SetCCWDirection():
	GPIO.output(DIR, CCW)

SetCWDirection()

delay = 0.005

instructions = " For plastic press '1'\n For glass press '2' \n For paper press '3' \n For organic waste press '4' \n"

def rotate(angle):
	SetCWDirection()
	for x in range(int(angle/AnglePerStep)):   # rotate the motor to the selected angle
		GPIO.output(STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(STEP, GPIO.LOW)
		sleep(delay)
		print("step #" + str(x+1) + " completed")  # print statement to follow after the stepping procedure
		12
	sleep(1.0)
	SetCCWDirection()  # revert the direction
	
	for x in range(int(angle/AnglePerStep)):   # rotate the motor back to its initial position
		GPIO.output(STEP, GPIO.HIGH)
		sleep(delay)
		GPIO.output(STEP, GPIO.LOW)
		sleep(delay)
		
	SetCWDirection()
	
	
#print(instructions) # print instructions	
#while True:
	#if keyboard.is_pressed("1"):
#		print(instructions)
#	if keyboard.is_pressed("2"):
#		rotate(180)
#		print(instructions)
#	if keyboard.is_pressed("3"):
##	if keyboard.is_pressed("4"):
	#	rotate(330)
	#	print(instructions)

while True:
	rotate(360)
