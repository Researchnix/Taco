#
#  Bundle.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Street

class Bundle:

    vertices = None
    ID = None
    length = None
    associatedStreets = []
    volume = 0


    def __init__(self, s):
        self.ID = "b" + s.ID[1:]
        self.length = s.length
        self.associatedStreets.append(s.ID)
        self.vertices = sorted([s.fromID, s.toID])


    def associateStreet(self, s):
        if (not s.ID in self.associatedStreets) and sorted([s.fromID, s.toID]) == self.vertices and self.length == s.length:
            self.associatedStreets.append(s.ID)
            return True
        else:
            return False

