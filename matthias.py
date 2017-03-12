import time
import MyMap
import Map
import RandomRoute

if __name__ == "__main__":
    t = time.time()

    karte = Map.Map("test1_street", "test1_inter")
    rg = RandomRoute.RandomRoute(karte)
    print rg.__getRoute__(3)



    print "\n\nDone in " + str(time.time() - t) + " s"
