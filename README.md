# Magic Band Reader
An overview mixed with a how to of how I built my Magic Band reader. 
## Introduction
I have seen a few people make these for themselves, but they lacked a good source of documentation for how and what they did.
My goal is to document what I do, the parts I use, and the code I write so that anyone can pick up this repo and do it themselves.
## Part 1 -- Where to begin
I first began looking around for YouTube videos and guides to see if anyone else had done this, and while I found a few, nobody with a step by step proccess to follow. I did get a lot of good ideas from watching these videos and will link them below.
## Part 2 -- BOM (Bill of Materials/Parts I used)
- (1) Raspberry Pi (these are hard to come by with the chip shortage) [click here](https://www.adafruit.com/product/3055)
- (10/15) female/feaml wires [click here](https://www.adafruit.com/product/1950)
- (1) RFID RC522 [click here](https://www.aliexpress.com/item/33020752786.html?srcSns=sns_Copy&spreadType=socialShare&bizType=ProductDetail&social_params=20471636797&aff_fcid=0a344a8fd7764ed2adabea1380accb8b-1643829764852-08588-_mOiFn48&tt=MG&aff_fsk=_mOiFn48&aff_platform=default&sk=_mOiFn48&aff_trace_key=0a344a8fd7764ed2adabea1380accb8b-1643829764852-08588-_mOiFn48&shareId=20471636797&businessType=ProductDetail&platform=AE&terminal_id=43bf1b4ddebe493197516fa3e3babe5f)
- (1) Neo Pixel LED strip [click here](https://www.adafruit.com/product/3919)
- (1) female DC Power adapter [click here](https://www.adafruit.com/product/368)
- (1) 5V 2A Switching Power Supply [click here](https://www.adafruit.com/product/276)

Be aware that the RFID RC522 is coming from AliExpress and it is not express, will take about 2 months to show up. The first RC522 I ordered was from Amazon and did not read actual magic bands, but was good enough to test the programing with [click here for that one](https://www.amazon.com/dp/B07KGBJ9VG?ref=ppx_yo2_dt_b_product_details&th=1)

## Part 3 -- Wiring it up
Follow the diagram below:
![image](https://github.com/astreich4/magic-band-reader/blob/main/Wiring/wiringDiagram.png)
Or if you like pictures more follow these pictures:
(Note: You cannot connect the led DIN wire to GPIO18, it will not work even though thats what the Adafruit guide says to do...)
![image](https://github.com/astreich4/magic-band-reader/blob/main/Wiring/RC522_Wiring.png)
![image](https://github.com/astreich4/magic-band-reader/blob/main/Wiring/NeoPixel_Wiring.png)

## Part4 -- Code
Once you have everything wired up, its time to test that everything works correctly.  
Note you will need to connect your pi to the internet to complete this.

#### RC522
The link for the guide that I followed is [here](https://pimylifeup.com/raspberry-pi-rfid-rc522/), but I will also go over all the steps.
1. Make sure that you enable the SPI interface (default is disabled) Run the below command and navigate to turn it on.
```
sudo raspi-config
```
2. Once this is done, reboot the Pi.
```
sudo reboot
```
3. Run the below command and if you see spi_bcm2835 then you are good, otherwise refer to the above guide.
```
lsmod | grep spi
```
4. Make sure the Pi is up to date.
```
sudo apt update
sudo apt upgrade
```
5. Now install python3 and pip.
```
sudo apt install python3-dev python3-pip
```
6. The library to interact with the device is the spidev library. Install by running:
```
sudo pip3 install spidev
```
7. Also needed is the MFRC522 library
```
sudo pip3 install mfrc522
```
8. Once this is done you can run the file `rfidtest.py` located in the code directory.
```
sudo python3 rfidtest.py
```
The program now waits for you to place your card on the scanner, once you do this you should see some numbers print on the screen and the program finish. If not review the above steps and try again.

#### LED
The guide that I used is located [here](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage), but again I will cover the important steps.  
NOTE: This guide assumes your LED strip has 30 LEDs if it has more or less you will need to change the code.
1. Assuming you ar following this in order you should have pip3 installed, so run the bellow commands:
```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

sudo python3 -m pip install --force-reinstall adafruit-blinka
```
2. Now you can run the `ledtest.py` file located in the code directory:
```
sudo python3 ledtest.py
```
This should turn the whole LED strip green for 5 seconds then turn it off. If this does not work, repeat the steps or refer to the linked guide.

#### Combined Testing
1. Run the `combinedtest.py` file in the code directory
```
sudo python3 combinetest.py
```
The program will now wait for you to scan your RFID tag, then light up green for 3 seconds, then turn off.  























