import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()


def read():
	id, text = reader.read()
	print(id)
	print(text)
	return True

