#
#  Map.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#
import FourWay
import Street
import Car
from random import *


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
            print line
            print "adding the intersection ", line[0]
            self.intersections[line[0]] = FourWay.FourWay(line[0], int(line[1]), int(line[2]))
        print self.intersections
        f.close()
        f = open(fileStreets, 'r')
        for line in f:
            line = line.split()
            print line
            # 0 street id
            # 1 length of street
            # 2 outgoing intersection
            # 3 incoming intersection

            newst = Street.Street(line[0], int(line[1]), line[2], line[3])
            self.streets[line[0]] = newst
        f.close()

        street = Street.Street("dhawu", 234, "i1", "i3")
        self.intersections["i1"].addOutgoing(street)
        #print self.intersections["i1"].outgoing

        """
        print self.streets
        for s in self.streets.values():
            self.intersections[s.fromID].addOutgoing(s)
        """

        for i in self.intersections.values():
            for o in i.outgoing:
                print o.ID
            print "\n\n"

        """
        example = Street.Street("test", 10, "i1", "i2")
        print "This is our test intersection"
        print self.intersections["i1"].incoming
        self.intersections["i1"].addIncoming(example)
        print self.intersections["i1"].incoming
        """

        """
            self.intersections[line[2]].addOutgoing(newst)
            self.intersections[line[3]].addIncoming(newst)
        f.close()
        print "all done!"
        """

    # Spawns the passed car on the specified street, returns true if successful, false if not
    def spawnCar(self, car):
        return self.streets.get(car.destination, False).queueCar(car)

    # Spawns a car with random route at a random street
    def spawnRandomCar(self):
       street1 = self.streets.values()[randint(0,len(self.streets.values())-1)]
       street2 = self.streets.values()[randint(0,len(self.streets.values())-1)]
       name = "car" + str(randint(0,99999999999999999))
       car = Car.Car(name, street1.ID, street2.ID)
       street1.queueCar(car)

