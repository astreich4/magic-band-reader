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
