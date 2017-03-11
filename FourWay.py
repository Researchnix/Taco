#
#  FourWay.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Intersection
import Street

class FourWay(Intersection.Intersection):
    waitingCars = 
    
    def __init__ (self, ID, x, y):
        self.ID = ID
        self.xPos = x
        self.yPos = y

    # Attach a new street as incoming, but only if there are less than 4
    def attachInStreet(self, s):
        if len(self.incoming) < 4:
            super(FourWay, self).attachInStreet(s)



    # Attach a new street as outgoing, but only if there are less than 4
    def attachOutStreet(self, s):
        if len(self.outgoing) < 4:
            super(FourWay, self).attachOutStreet(s)



    # Do a time step, which means:
    #       Update traffic lights
    #       Try pushing cars in streets
    #       Ask streets to dequeue cars
    def timeStep(self):
