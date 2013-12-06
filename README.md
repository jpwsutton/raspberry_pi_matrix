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

The Datasheet for these displays can be seen [here](http://www.embeddedadventures.com/datasheets/LDP-6432.pdf), however I will do my best to ~~explain~~ (Basically copy) the protocol here too.



Hardware
--------
In order to use this LED matrix, you **WILL** need an external 5V power supply, something that can produce at least 4A, otherwise it will not be able to light up fully and you may damage it.

The raspberry pi can still be powered the same way you usually do (5V USB).Both devices should share a ground line though.

### GPIO Pins:
There is no *special* order for these pins, I just chose them as I wired up the display. It will be possible however, to use different pins if you so wish.

| GPIO Pin | Display Pin |
|:--------:|:-----------:|
| 4        | EN          |
| 7        | A           |
| 8        | B           |
| 9        | C           |
| 10       | D           |
| 17       | R1          |
| 18       | S           |
| 21 (22 on R2 boards)      | R2          |
| 23       | L           |
| 24       | G2          |
| 25       | G1          |


Protocol
--------

### Pin States:

To display a particular row, the pins A,B,C and D are used as follows:

| D | C | B | A | Row Enabled |
|:-:|:-:|:-:|:-:|:------------|
| 0 | 0 | 0 | 0 | 0 (Top Row) and 16 |
| 0 | 0 | 0 | 1 | 1 and 17 |
| 0 | 0 | 1 | 0 | 2 and 18 |
| 0 | 0 | 1 | 1 | 3 and 19 |
| 0 | 1 | 0 | 0 | 4 and 20 |
| 0 | 1 | 0 | 1 | 5 and 21 |
| 0 | 1 | 1 | 0 | 6 and 22 |
| 0 | 1 | 1 | 1 | 7 and 23 |
| 1 | 0 | 0 | 0 | 8 and 24 |
| 1 | 0 | 0 | 1 | 9 and 25 |
| 1 | 0 | 1 | 0 | 10 and 26 |
| 1 | 0 | 1 | 1 | 11 and 27 |
| 1 | 1 | 0 | 0 | 12 and 28 |
| 1 | 1 | 0 | 1 | 13 and 29 |
| 1 | 1 | 1 | 0 | 14 and 30 |
| 1 | 1 | 1 | 1 | 15 and 31 (Bottom Row) |


To Set pixels within a row, the following pins are used.


| Pin | Function |
|:---:|:--------:|
| R1 | Data for RED LED in pixel in upper 16 rows. |
| G1 | Data for GREEN LED in pixel in upper 16 rows. |
| R2 | Data for RED LED in pixel in lower 16 rows. |
| G2 | Data for GREEN LED in pixel in lower 16 rows. |
| S | Shift Data. |
| L | Latch Data. |


These lines are active low, so set to 0 in order to light an led and 1 to turn an led off.


To Enable the display 

|    |                             |
|:--:|:---------------------------:|
| EN | Enable Display (Active low) |


### Using the Display



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
