import time

t_end = time.time() + 4
while time.time() < t_end:
	for x in range(0,20):
		time.sleep(0.05)
		print((x-1)%20)
			# pixels[x] = (0,255,0)
			# pixels[(x+1)%20] = (0,255,0)
			# pixels[(x+2)%20] = (0,255,0)
			# pixels[(x+3)%20] = (0,255,0)
			# pixels[(x+4)%20] = (0,255,0)
			# pixels[(x+5)%20] = (0,0,0)