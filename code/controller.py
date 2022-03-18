import rfidcontroller
import ledcontroller

try:
	while True:
		rfid = rfidcontroller.read
		if rfid == True:
			ledcontroller.lightup
			rfid = False