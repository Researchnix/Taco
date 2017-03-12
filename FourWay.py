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
    incoming = []
    outgoing = []
    waitingCars = {}
    queueSize = 5       # Number of cars that can wait in each queue
    trali = 0
    
    def __init__ (self, ID, x, y):
        self.ID = ID
        self.xPos = x
        self.yPos = y
        trali = TrafficLight.TrafficLight(4,4)

    def initializeTrafficLight(self):


    # Attach a new street as incoming
    def attachInStreet(self, s):
        self.incoming.append(s)
        for a in self.waitingCars.values():
            a[s.ID] = collections.deque([])


    # Attach a new street as outgoing
    def attachOutStreet(self, s):
        self.outgoing.append(s)
        self.waitingCars[s.ID] = {}
        for u in self.incoming:
            self.waitingCars[s.ID][u.ID] = collections.deque([])

    # Do a time step, which means:
    #       Update traffic lights
    #       Try to queue cars in streets
    #       Ask streets to dequeue cars
    def timeStep(self, time):
        self.trali.update(time) # Only a dummy for now
        

        # Try to queue cars in streets
        # It depends 
        for s in self.outgoing:
            pass



        # Ask streets to dequeue cars
        for s in streets:
            newCar = s.inspectCar()
            if newCar != None:
                if len(self.waitingCars[newCar.nextStreet(), s.ID]) <= self.queueSize:
                    self.waitingCars[newCar.nextStreet(), s.ID].append(s.dequeueCar())
         

