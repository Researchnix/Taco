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

    # departure time stamp
    startTime = 0

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



    def __init__ (self, ID, start, destination, timestamp=0, route = None):
        self.ID = ID
        self.start = start
        self.destination = destination
        self.startTime = timestamp
        if route is not None:
            StreetRoute = route
