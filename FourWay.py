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

    # Initialize this traffic light only after all streets are attached to this intersection
    def initializeTrafficLight(self):
        trali = TrafficLight.TrafficLight(self.incoming, self.outgoing)


    # Attach a new street as incoming
    def addIncoming(self, s):
        self.incoming.append(s)
        for a in self.waitingCars.values():
            a[s.ID] = collections.deque([])


    # Attach a new street as outgoing
    def addOutgoing(self, s):
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
        # It depends on the traffic light state
        for o in self.outgoing:
            for i in self.incoming:
                if trali.pathAllowed(o.ID, i.ID) and len(self.waitingCars[o.ID][i.ID]) != 0:
                    car = self.waitingCars[o.ID][i.ID].pop()
                    if not o.queueCar(car):
                        self.waitingCars[o.ID][i.ID].appendleft(car)
                        
                    



        # Ask streets to dequeue a car, if there is space in the specific queue
        # for this incoming street
        for s in self.incoming:
            if max([len(x[s.ID]) for x in self.waitingCars]) <= self.queueSize:
                newCar = s.dequeueCar()
                if newCar != None:
                    self.waitingCars[newCar.nextStreet(), s.ID].append(newCar)
         

