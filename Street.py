#
#  Street.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import collections
import BookKeeper


class Street:

    # Street ID
    ID = ""

    # Neighbouring intersection IDs
    fromID = ""
    toID = ""

    # Street length determines time required to pass through the road, as well as its capacity
    length = 10

    # Amount of cars currently on the street
    carAmount = 0

    # The part of the street that is not occupied and can quickly be passed through
    flexQueue = collections.deque([])

    # The cars stack up in this queue after passing through the free section
    standingQueue = collections.deque([])

    # The global bookkeeper
    tracker = None

    def __init__(self, ID, length, fromID = None, toID = None):
        self.ID = ID
        self.length = length
        self.fromID = fromID
        self.toID = toID
        for i in range(length):
            self.flexQueue.append(None)
        

    def setTracker(self, tracker):
        self.tracker = tracker

    # Adds a Car at the end of the queue, returns true if successful, false if street is full
    def queueCar(self, c):
        if self.carAmount >= self.length:
            return False
        else:
            c.history.append(self.ID)
            if c.peekNextSt() is None or c.peekNextSt is self.ID:
                self.tracker.trackCar(c)
            else:
                flexFirst = self.flexQueue.popleft()
                if flexFirst is not None:
                    self.standingQueue.append(flexFirst)
                self.flexQueue.append(c)
                self.carAmount += 1
            return True

    # Returns a car from the front of the queue, None if street is empty
    def dequeueCar(self):
        self.carAmount -= 1
        self.flexQueue.append(None)
        if len(self.standingQueue) != 0:
            return self.standingQueue.popleft()
        else:
            return None

    # Moves cars up the street into queue
    def update(self):
        flexFirst = self.flexQueue.popleft()
        if flexFirst is None:
            self.flexQueue.append(None)
        else:
            self.standingQueue.append(flexFirst)


    # Returns amount of cars currently on street
    def getCarAmount(self):
        return self.carAmount

    # Returns the ratio of cars on street/ street length
    def getPctFull(self):
        return float(self.carAmount) / self.length


