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
import BookKeeper
import Timer



if __name__ == "__main__":
    t = time.time()

    timer = Timer.Timer()
    keeper = BookKeeper.BookKeeper("log.txt", timer)

    f = FourWay.FourWay("id", 1, 2)
    car = Car.Car("a", "s36", "s78", 3)
    r = Street.Street("r", 10)


    karte = Map.Map("test1_street", "test1_inter", keeper)
    karte.show()

    tran = Transmitter.Transmitter(karte.intersections, karte.streets)
    tran.streetTransmit(karte.intersections, karte.streets)
    tran.intersectionTransmit(karte.intersections)

    print "\n\n\n"
    exFW = karte.intersections.values()[0]
    print exFW.trali
    


    print "\n\nDone in " + str(time.time() - t) + " s"
