#
#  main.py
#  Taco  ---  SPH Innovation Challenge
#
#  Created by Mat, Kon and Len on 2017-03-11.
#  Copyright 2016 Researchnix. All rights reserved.
#

import sys
import time
import FourWay
import Car
import Street
import Map
import Transmitter



if __name__ == "__main__":
    t = time.time()


    f = FourWay.FourWay("id", 1, 2)
    car = Car.Car("a", "s36", "s78", 3)
    r = Street.Street("r", 10)


    karte = Map.Map("test1_street", "test1_inter")
    karte.show()
    karte.spawnCar(car)

    tran = Transmitter.Transmitter()
    print tran.streetTransmit(karte.intersections, karte.streets)
    


    print "\n\nDone in " + str(time.time() - t) + " s"
