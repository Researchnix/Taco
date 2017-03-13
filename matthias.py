import time
import Map
import Timer
import BookKeeper
import RandomRoute

if __name__ == "__main__":
    t = time.time()
    timer = Timer.Timer()
    keeper = BookKeeper.BookKeeper("log.txt", timer)
    karte = Map.Map("test1_street", "test1_inter", keeper)
    for i in range(1000):
        karte.spawnDummyCar()
        karte.update()
        timer.increment()





    print "\n\nDone in " + str(time.time() - t) + " s"
