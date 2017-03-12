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


if __name__ == "__main__":
    t = time.time()


    f = FourWay.FourWay("id", 1, 2)

    print "\n\nDone in " + str(time.time() - t) + " s"
