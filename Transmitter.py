#
#  Transmitter.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import json
import Bundle
import FourWay

class Transmitter:

    bundles = []

    def __init__(self, intersections, streets):
        self.bundles = self.bundle(streets)

    def streetTransmit(self, intersections, streets):
        self.update(streets)
        streetContainer = {}
        for b in self.bundles:
            streetContainer[b.ID] = {
                        'id' : b.ID,
                        'from' : { 'x' : intersections[b.vertices[0]].xPos,
                                    'y' : intersections[b.vertices[0]].yPos
                                },
                        'to' : { 'x' : intersections[b.vertices[1]].xPos,
                                    'y' : intersections[b.vertices[1]].yPos
                                },
                        'percent' : b.volume
                                    }
        print json.dumps(streetContainer)


    def intersectionTransmit(self, intersections):
        intersectionContainer = {}
        for i in intersections.values():
            intersectionContainer[i.ID] = {
                        'id' : i.ID,
                        'x' : i.xPos,
                        'y' : i.yPos,
                        'inStreets' : [s.ID for s in i.incoming],
                        'OutStreets' : [s.ID for s in i.outgoing],
                        'open' : filter(lambda x : i.trali.pathAllowed(x[0], x[1]), [[a.ID, b.ID] for a in i.incoming for b in i.outgoing])
                                            }
        print json.dumps(intersectionContainer)


    def update(self, streets):
        for b in self.bundles:
            b.volume = sum([streets[ID].getPctFull() for ID in b.associatedStreets])


    def bundle(self, streets):
        bundles = []
        for s in streets.values():
            if not (True in [b.associateStreet(s) for b in bundles]):
                bundles.append(Bundle.Bundle(s))
        return bundles
            
            
