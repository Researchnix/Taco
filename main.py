import time
import Map
import RandomRoute

if __name__ == "__main__":
    t = time.time()
    pSpawn = 0.4
    karte = Map.Map("test1_street", "test1_inter")
    rg = RandomRoute.RandomRoute(karte)




    print "\n\nDone in " + str(time.time() - t) + " timesteps"
