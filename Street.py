#
#  Street.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Car.Car
import collections

class Street:
    ID = ""
    length = 10
    carAmount = 0
    flexQueue = collections.deque([])
    standingQueue = collections.deque([])



    def __init__ (self, ID, length):
        self.ID = ID
        self.length = length

#Adds a Car at the end of the queue, returns true if successful, false if street is full
    def queueCar(self, c):
        if self.carAmount >= self.length:
            return False
        else:
            flexFirst = self.flexQueue.popleft()
            if flexFirst is not None:
                self.standingQueue.append(flexFirst)
            self.flexQueue.append(c)
            self.carAmount += 1
            return True


    def dequeueCar(self):
        self.carAmount -= 1
        self.flexQueue.append(None)
        return self.standigQueue.popleft()

    def update(self):
        flexFirst = self.flexQueue.popleft()
        if flexFirst is None:
            self.flexQueue.append(None)
        else:
            self.standingQueue.append(flexFirst)



    def getCarAmount(self):
        return self.carAmount

    def getPctFull(self):
        return (float)(self.carAmount) / self.length


