import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

servo1.start(0)
print("waiting for 2 seconds")
time.sleep(2)

duty = 2

while duty <= 12:
		servo1.ChangeDutyCycle(duty)
		time.sleep(.3)
		duty = duty +1

print("Done")