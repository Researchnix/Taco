#
#  Map.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#
import Intersection
import Street

class Map:

    intersections = []
    streets = []

    def __init__(self, fileStreets, fileInter):

        f = open(fileInter, 'r')
        for line in f:
            line = line.split()
            x = Intersection()
            self.intersections.append(Intersection(int(line[0]), int(line[1]), int(line[2])))


