
class Timer:

    time = 0
    events = []

    def increment(self):
        self.time += 1

    def get(self):
        return self.time

    def recordevent(self):
        self.events.append(self.time)