#!/usr/bin/env python

import time
import datetime

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

class Clock:
    def __init__(self):
        unicorn.rotation(90)
        unicorn.brightness(0.1)


    # Composition methods
    def fullLine(start, row):
        for x in range(start, start+7):
            unicorn.set_pixel(x, row, 255, 255, 255)

    def bothSides(start, row):
        unicorn.set_pixel(start, row, 255, 255, 255)
        unicorn.set_pixel(start+6, row, 255, 255, 255)

    def leftSide(start, row):
        unicorn.set_pixel(start, row, 255, 255, 255)

    def rightSide(start, row):
        unicorn.set_pixel(start+6, row, 255, 255, 255)

    # Numbers
    def displayZero(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.bothSides(x, y-1)
        self.bothSides(x, y-2)
        self.bothSides(x, y-3)
        self.bothSides(x, y-4)
        self.bothSides(x, y-5)
        self.fullLine(x, y-6)
        unicorn.show()

    def displayOne(x, y):
        self.clearNumberPixels(x, y)
        self.rightSide(x, y)
        self.rightSide(x, y-1)
        self.rightSide(x, y-2)
        self.rightSide(x, y-3)
        self.rightSide(x, y-4)
        self.rightSide(x, y-5)
        self.rightSide(x, y-6)
        unicorn.show()

    def displayTwo(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.rightSide(x, y-1)
        self.rightSide(x, y-2)
        self.fullLine(x, y-3)
        self.leftSide(x, y-4)
        self.leftSide(x, y-5)
        self.fullLine(x, y-6)
        unicorn.show()

    def displayThree(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.rightSide(x, y-1)
        self.rightSide(x, y-2)
        self.fullLine(x, y-3)
        self.rightSide(x, y-4)
        self.rightSide(x, y-5)
        self.fullLine(x, y-6)
        unicorn.show()

    def displayFour(x, y):
        self.clearNumberPixels(x, y)
        self.bothSides(x, y)
        self.bothSides(x, y-1)
        self.bothSides(x, y-2)
        self.fullLine(x, y-3)
        self.rightSide(x, y-4)
        self.rightSide(x, y-5)
        self.rightSide(x, y-6)
        unicorn.show()

    def displayFive(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.leftSide(x, y-1)
        self.leftSide(x, y-2)
        self.fullLine(x, y-3)
        self.rightSide(x, y-4)
        self.rightSide(x, y-5)
        self.fullLine(x, y-6)
        unicorn.show()

    def displaySix(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.leftSide(x, y-1)
        self.leftSide(x, y-2)
        self.fullLine(x, y-3)
        self.bothSides(x, y-4)
        self.bothSides(x, y-5)
        self.fullLine(x, y-6)
        unicorn.show()

    def displaySeven(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.rightSide(x, y-1)
        self.rightSide(x, y-2)
        self.rightSide(x, y-3)
        self.rightSide(x, y-4)
        self.rightSide(x, y-5)
        self.rightSide(x, y-6)
        unicorn.show()

    def displayEight(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.bothSides(x, y-1)
        self.bothSides(x, y-2)
        self.fullLine(x, y-3)
        self.bothSides(x, y-4)
        self.bothSides(x, y-5)
        self.fullLine(x, y-6)
        unicorn.show()

    def displayNine(x, y):
        self.clearNumberPixels(x, y)
        self.fullLine(x, y)
        self.bothSides(x, y-1)
        self.bothSides(x, y-2)
        self.fullLine(x, y-3)
        self.rightSide(x, y-4)
        self.rightSide(x, y-5)
        self.fullLine(x, y-6)
        unicorn.show()

    def displayNumber(x,y, number):
        if number == 0:
            self.displayZero(x,y)
        elif number == 1:
            self.displayOne(x,y)
        elif number == 2:
            self.displayTwo(x,y)
        elif number == 3:
            self.displayThree(x,y)
        elif number == 4:
            self.displayFour(x,y)
        elif number == 5:
            self.displayFive(x,y)
        elif number == 6:
            self.displaySix(x,y)
        elif number == 7:
            self.displaySeven(x,y)
        elif number == 8:
            self.displayEight(x,y)
        elif number == 9:
            self.displayNine(x,y)

    # Clears the pixels in a rectangle. x,y is the top left corner of the rectangle
    # and its dimensions are 7X7
    def clearNumberPixels(x, y):
        for y1 in range(y, y-7, -1):
            for x1 in range(x, x+7):
                # print("x1 = "+str(x1)+" y1 = "+str(y1))
                unicorn.set_pixel(x1, y1, 0, 0, 0)
        unicorn.show()



    # Gets a specific part of the current time, passed to strftime, then it is
    # split into its individual numbers and converted into integers. Used to feed
    # the display with numbers

    def getTimeParts(timePart):
        parts = datetime.datetime.now().strftime(timePart)
        return [int(x) for x in parts]  

    displayedHourParts = self.getTimeParts('%H')
    displayedMinuteParts = self.getTimeParts('%M')

    # Display Current Time
    self.displayNumber(0,15, displayedHourParts[0])
    self.displayNumber(8,15, displayedHourParts[1])
    self.displayNumber(0,6, displayedMinuteParts[0])
    self.displayNumber(8,6, displayedMinuteParts[1])


    try:
        while True:
            hourParts = self.getTimeParts('%H')
            minuteParts = self.getTimeParts('%M')
    
            # TIME Details
            # Only update first hour number if it is different to what is currently displayed
            if hourParts[0] != displayedHourParts[0]:
                displayedHourParts[0] = hourParts[0]
                self.displayNumber(0,15, hourParts[0])

            # Only update second hour number if it is different to what is currently displayed
            if hourParts[1] != displayedHourParts[1]:
                displayedHourParts[1] = hourParts[1]
                self.displayNumber(8,15, hourParts[1])

            # Only update first minute number if it is different to what is currently displayed
            if minuteParts[0] != displayedMinuteParts[0]:
                displayedMinuteParts[0] = minuteParts[0]
                self.displayNumber(0,6, minuteParts[0])

            # Only update second minute number if it is different to what is currently displayed
            if minuteParts[1] != displayedMinuteParts[1]:
                displayedMinuteParts[1] = minuteParts[1]
                self.displayNumber(8,6, minuteParts[1])

            # Sleep for 0.5 because the display doesn't need to update that often
            time.sleep(1)
    
    except KeyboardInterrupt:
        unicorn.off()
