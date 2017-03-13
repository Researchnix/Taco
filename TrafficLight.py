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
    state = {}



    def __init__(self, incoming, outgoing):
        for o in outgoing:
            self.state[o.ID] = {}
            for i in incoming:
                self.state[o.ID][i.ID] = True

    # For now every state is 1, so every car can go anywhere
    def setState(self):
        pass

    # Dummy function, should actually decide if
    # if a path on the intersection is clear
    # depending on its current state
    def pathAllowed(self, i, o):
            return self.state[o][i]


    # Another dummt functio
    def update(self, time):
        pass


