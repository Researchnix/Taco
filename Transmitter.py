#
#  Transmitter.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import json

class Transmitter:


    def streetTransmit(self, intersections, streets):
        streetContainer = {}
        for s in streets.values():
            streetContainer[s.ID] = {
                        'id' : s.ID,
                        'from' : { 'x' : intersections[s.fromID].xPos,
                                    'y' : intersections[s.fromID].yPos
                                },
                        'to' : { 'x' : intersections[s.toID].xPos,
                                    'y' : intersections[s.toID].yPos
                                }

                                    }
        return json.dumps(streetContainer)


    def intersectionTransmit(self, intersections):
        intersectionContainer = {}
        for i in intersections.values():
            intersectionContainer[i.ID] = {
                        'id' : i.ID,
                        'x' : i.xPos,
                        'y' : i.yPos,
                        'streets' : [s.ID for s in i.incoming] + [s.ID for s in i.outgoing],
                        # TODO make this not a dummy
                                            }
        return json.dumps(streetContainer)

