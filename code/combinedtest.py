import time
import board
import neopixel
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
pixels = neopixel.NeoPixel(board.D18, 30)


try:
	id, text = reader.read()
	print(id)
	print(text)
	pixels.fill((0, 255, 0))
	time.sleep(3000)
	pixels.fill((0, 0, 0))
finally:
	GPIO.cleanup()