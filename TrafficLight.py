#
#  TrafficLight.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

class TrafficLight:

    # State is a 2D array with the values 0 and 1 associating red and green
    # to the path from one incoming street to another outgoing street
    state = 0



    def __init__(self, numberIn, numberOut):
        self.state = [[0 for i in range(numberIn)] for j in range(numberOut)]

        
    def setState(self, ):
        self.state = s


    # Dummy function, should actually decide if
    # if a path on the intersection is clear
    # depending on its current state
    def pathAllowed(self, a, b):
        return True


    # Another dummt functio
    def update(self, time):
        pass


