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
    percentFilled = 0.0
    flexQueue = collections.deque([])
    standingQueue = collections.deque([])



    def __init__ (self, ID, length):
        self.ID = ID
        self.length = length



    def queueCar(self, c):
        if self.carAmount >= self.length:
            return False
        else:
            self.flexQueue.append(c)

            self.carAmount += 1
            return True


    def dequeueCar(self):

    def update(self):



    def getCarAmount(self):



