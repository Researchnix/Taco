#
#  TrafficLight.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

class TrafficLight:

    state = 0


    def setState(self, s):
        self.state = s


    # Dummy function, should actually decide if
    # if a path on the intersection is clear
    # depending on its current state
    def pathAllowed(self, a, b):
        return True


