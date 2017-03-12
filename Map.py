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

    intersections = {}
    streets = {}

    # Reads the specified files and initializes the graph.
    # Intersection file format: ID, xPos, yPos
    # Street file format: ID, length, from, to
    def __init__(self, fileStreets, fileInter):
        f = open(fileInter, 'r')
        for line in f:
            line = line.split()
            self.intersections[line[0]] = Intersection.Intersection(line[0], int(line[1], int(line[2])))
        f = open(fileStreets, 'r')
        for line in f:
            line = line.split()
            newst = Street.Street(line[0], line[1], line[2], line[3])
            self.streets[line[0]] = Street.Street(newst)
            self.intersections[line[2]].addOutgoing(newst)
            self.intersections[line[3]].addIncoming(newst)
        f.close()

