
import Car
import Timer

class BookKeeper:

    logfile = None
    timer = None

    def __init__(self, logfile, timer):
        self.logfile = logfile
        f = open(logfile, 'w')
        f.write("Bookkeeper initialized.")
        f.close()
        self.timer = timer

    def trackCar(self, c):
        c.arrive(self.timer.get())
        f = open(self.logfile, 'a')
        f.write(c.ID + '- dep: ' + c.startTime + ', arr: ' + c.endTime + ', time: '
                + c.totalTime + ', route: ' + str(c.StreetRoute))
