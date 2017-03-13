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
    timer = None

    # Reads the specified files and initializes the graph.
    # Intersection file format: ID, xPos, yPos
    # Street file format: ID, length, from, to
    def __init__(self, fileStreets, fileInter, bookKeeper):
        """ Reading the intersection file """
        f = open(fileInter, 'r')
        for line in f:
            line = line.split()
            self.intersections[line[0]] = FourWay.FourWay(line[0], int(line[1]), int(line[2]))
        f.close()

        """ Reading the street file """
        f = open(fileStreets, 'r')
        for line in f:
            line = line.split()
            newst = Street.Street(line[0], int(line[1]), line[2], line[3])
            newst.setTracker(bookKeeper)
            self.streets[line[0]] = newst
        f.close()

        """ Add all streets to the intersections """
        for s in self.streets.values():
            self.intersections[s.fromID].addOutgoing(s)
            self.intersections[s.toID].addIncoming(s)

        """ Initialize Traffic Lights """
        for inter in self.intersections.values():
            inter.initializeTrafficLight()


    def update(self):
        for street in self.streets.values():
            street.update()
        for inter in self.intersections.values():
            inter.update()

    def show(self):
        for i in sorted(self.intersections.values()):
            print i.ID, sorted([s.ID for s in i.incoming] + [s.ID for s in i.outgoing])

    # Spawns the passed car on the specified street, returns true if successful, false if not
    def spawnCar(self, car):
        target = self.streets.get(car.dequeueNextSt())
        return target.queueCar(car)

    # Spawns a car with random route at a random street
    def spawnRandomCar(self):
       street1 = self.streets.values()[randint(0,len(self.streets.values())-1)]
       street2 = self.streets.values()[randint(0,len(self.streets.values())-1)]
       name = "car" + str(randint(0,99999999999999999))
       car = Car.Car(name, street1.ID, street2.ID)
       street1.queueCar(car)

    def spawnDummyCar(self):
        c = Car.Car("test", 0, 0, 0, [])
        randomst = self.streets.values()[randint(0, len(self.streets.values()) - 1)]
        randomst.queueCar(c)
