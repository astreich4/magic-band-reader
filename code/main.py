import time
import board
import neopixel
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

num_pixels = 20
reader = SimpleMFRC522()
pixels = neopixel.NeoPixel(board.D21, num_pixels)

def run():
	t_end = time.time() + 4
	while time.time() < t_end:
		for x in range(0,20):
			time.sleep(0.05)
			pixels[x] = (0,0,0)
			pixels[(x+1)%20] = (0,255,0)
			pixels[(x+2)%20] = (0,255,0)
			pixels[(x+3)%20] = (0,255,0)
			pixels[(x+4)%20] = (0,255,0)
			pixels[(x+5)%20] = (0,255,0)

try:
	id, text = reader.read()
	print(id)
	print(text)
	run()
finally:
	GPIO.cleanup()


