#
#  FourWay.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Car
import Street
import TrafficLight
import collections

class FourWay:
    ID = ""
    xPos = 0
    yPos = 0
    incoming = {}
    outgoing = {}
    waitingCars =
    trali = TrafficLight.TrafficLight()
    
    def __init__ (self, ID, x, y):
        self.ID = ID
        self.xPos = x
        self.yPos = y

    # Attach a new street as incoming
    def attachInStreet(self, s):
        self.incoming.append(s)


    # Attach a new street as outgoing
    def attachOutStreet(self, s):
        self.outgoing.append(s)


    # Do a time step, which means:
    #       Update traffic lights
    #       Try pushing cars in streets
    #       Ask streets to dequeue cars
    def timeStep(self, time):
        self.trali.update(time) # Only a dummy for now
        

        # Ask streets to dequeue cars
        for s in streets:

         
