import rfidcontroller
import ledcontroller


while True:
	rfid = rfidcontroller.read
	if rfid == True:
		ledcontroller.lightup
		rfid = False