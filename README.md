Raspberry Pi 32x64 R&G LED Display Driver
=========================================

A Python library to control a 32x64 LED Matrix with a raspberry pi

This code is mostly an experiment and is by no means complete or production ready.

This is licensed under the MIT license (See LICENSE)

Feel free to contact me at code@jsutton.co.uk
Follow me on twitter @jpwsutton

Overview
--------
The 32x54 R&G LED matrix panels that this project is targeted against can be purchased from [Embedded Adventures](http://www.embeddedadventures.com/led_matrix_display_LDP-6432.html).

It is effectively two 16x64 LED matrices in parallel, You address each 16 rows separately as will be described later.

The Datasheet for these displays can be seen [here](http://www.embeddedadventures.com/datasheets/LDP-6432.pdf), however I will do my best to explain the protocol here too.



Hardware
--------
In order to use this LED matrix, you **WILL** need an external 5V power supply, something that can produce at least 4A, otherwise it will not be able to light up fully and you may damage it.

The raspberry pi can still be powered the same way you usually do (5V USB).Both devices should share a ground line though.

### GPIO Pins:
There is no *special* order for these pins, I just chose them as I wired up the display. It will be possible however, to use different pins if you so wish.
* 4 -> EN
* 7 -> A
* 8 -> B
* 9 -> C
* 10 -> D
* 17 -> R1
* 18 -> S
* 21 (22 on R2 boards) -> R2
* 23 -> L
* 24 -> G2
* 25 -> G1


Protocol
--------


Running
-------


Tests
-----

Limitations
-----------


To Do
-----

- [ ] Descibe the protocol in the protocol section of this readme.
- [ ] Create the basic python module that will be used in the driver.
- [ ] Create a basic test script to test basic and in time, advanced functionality of the module.
