
import Car
import Timer

class BookKeeper:

    logfile = None

    def __init__(self, logfile, timer):
        self.logfile = logfile
        f = open(logfile, 'w')
        f.write("Bookkeeper initialized.")
        f.close()

    def trackCar(self, c):
        f = open(self.logfile, 'a')
        f.write(c.ID + '- dep: ' + c.startTime + ', arr: ' + c.endTime + ', time: ' + c.totalTime)