"""The Raspberry Pi driver for a 32x64 BiColour LED Matrix.

"""
class driver:
    """A Class to represent the Matrix Driver"""

    def __init__(self, **kwargs):
        """Initialises the driver, settings pins and such"""
        # Set The WiringPi Pins Based upon either the kwargs or the defaults
        self.pins_EN = kwargs.get('EN', 7)
        self.pins_A = kwargs.get('A', 11)
        self.pins_B = kwargs.get('B', 10)
        self.pins_C = kwargs.get('C', 13)
        self.pins_D = kwargs.get('D', 12)
        self.pins_R1 = kwargs.get('R1', 0)
        self.pins_R2 = kwargs.get('R2', 3)
        self.pins_S = kwargs.get('S', 1)
        self.pins_L = kwargs.get('L', 4)
        self.pins_G1 = kwargs.get('G1', 6)
        self.pins_G2 = kwargs.get('G2', 5)

	# Initialise WiringPi

	# Initialise the pins in WiringPi

        
    def drawArray(self, arrayToDraw):
        """Draws an array to the matrix"""


    def clearMatrix(self):
        """Draws a blank array to the matrix"""



    def joke(self):
        """Tells the funniest joke in the world, beware if you understand german!"""
        return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
                u'Beiherhund das Oder die Flipperwaldt gersput.')


    def listPins(self):
        print("Pin A is: " + str(self.pins_A))
