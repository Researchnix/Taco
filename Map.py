#
#  Map.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#
import Intersection
import Street
import Car


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
            self.intersections[line[0]] = Intersection.Intersection(line[0], int(line[1]), int(line[2]))
        f.close()
        f = open(fileStreets, 'r')
        for line in f:
            line = line.split()
            if line.__len__() < 4:
                break
            newst = Street.Street(line[0], int(line[1]), line[2], line[3])
            self.streets[line[0]] = newst
            self.intersections[line[2]].addOutgoing(newst)
            self.intersections[line[3]].addIncoming(newst)
        f.close()
        print "all done!"

    # Spawns the passed car on the specified street, returns true if successful, false if not
    def spawnCar(self, streetID, car):
        return self.streets.get(streetID, False).queueCar(car)

    # Spawns a car with random route at a random street
    #def spawnRandomCar(self, *ID):
    #   if ID is None:
    #      car = Car.Car()
