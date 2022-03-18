import time
import board
import neopixel
import RPi.GPIO as GPIO

num_pixels = 30
pixels = neopixel.NeoPixel(board.D21, num_pixels)




def lightup():
	t_end = time.time() + 2
	while time.time() < t_end:
		for x in range(0,20):
			time.sleep(0.01)
			pixels[x] = (0,0,0)
			pixels[(x+1)%20] = (0,255,0)
			pixels[(x+2)%20] = (0,255,0)
			pixels[(x+3)%20] = (0,255,0)
			pixels[(x+4)%20] = (0,255,0)
			pixels[(x+5)%20] = (0,255,0)
	pixels.fill((0, 255, 0))
	time.sleep(2)
	for x in range(0,20):
		time.sleep(0.05)
		pixels[x] = (0,0,0)
	pixels.fill((0, 0, 0))