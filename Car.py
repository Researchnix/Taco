#
#  Car.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#
import collections

class Car:

    # ID of the car
    ID = ""

    # starting point of the car
    start = 0

    # departure and arrival time stamps
    startTime = 0
    endTime = 0

    # total travel time
    totalTime = 0

    # destinatino of the car
    destination = 0

    # This should be a list of vertices that the needs to visit to reach
    # its desitination
    InterRoute = []

    # From the InterRoute one can simply obtain the StreetRoute,
    # by replacing the i and i+1 entry by the unique street leading
    # from i to i+1
    StreetRoute = []
    StreetQueue = collections.deque(StreetRoute)
    # nextStreet = StreetRoute[0]

    # record of actual roads visited
    history = []



    def __init__ (self, ID, start, destination, timestamp=0, route = None):
        self.ID = ID
        self.start = start
        self.destination = destination
        self.startTime = timestamp
        self.history = list([])
        if route is not None:
            self.StreetRoute = route
            self.StreetQueue = collections.deque(self.StreetRoute)

    def dequeueNextSt(self):
        try:
            return self.StreetQueue.popleft()
        except:
            return None

    def peekNextSt(self):
        try:
            return self.StreetQueue[0]
        except:
            return None

    def arrive(self, timestamp):
        self.endTime = timestamp
        self.totalTime = self.endTime - self.startTime
