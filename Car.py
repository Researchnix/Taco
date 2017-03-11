#
#  Car.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

class Car:
    # ID of the car
    ID = ""
    # starting point of the car
    start = 0
    # destinatino of the car
    destination = 0
    # This should be a list of vertices that the needs to visit to reach
    # its desitination
    InterRoute = []
    # From the InterRoute one can simply obtain the StreetRoute,
    # by replacing the i and i+1 entry by the unique street leading
    # from i to i+1
    StreetRoute[]
    # nextStreet = StreetRoute[0]



    def __init__ (self, ID, start, destination):
        self.ID = ID
        self.start = start
        self.destination = destination
