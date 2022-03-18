import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)
reader = SimpleMFRC522()


def read():
	try:
		id, text = reader.read()
		print(id)
		print(text)
	finally:
		GPIO.cleanup()
	return True

