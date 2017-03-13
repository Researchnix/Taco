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
    karte = Map.Map("test1_street", "test1_inter", keeper)

    print "map initialized"

    tran = Transmitter.Transmitter(karte.intersections, karte.streets)
    karte.show()

    for i in range(100):
        karte.spawnRandomCar()
        karte.update()
        tran.streetTransmit(karte.intersections, karte.streets)
        tran.intersectionTransmit(karte.intersections)
        timer.increment()
        print "\n"



    


    print "\n\nDone in " + str(time.time() - t) + " s"
