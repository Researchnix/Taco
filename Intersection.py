#
#  Intersection.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

class Intersection:
    ID = ""
    xPos = 0
    yPos = 0
    incoming = []
    outgoing = []


    def __init__ (self, ID, x, y):
        self.ID = ID
        self.xPos = x
        self.yPos = y


    # Attach a new street as incoming
    def attachInStreet(self, s)
        incoming
