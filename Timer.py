
class Timer:

    time = 0
    events = []

    def increment(self):
        self.time += 1

    def get(self):
        return self.time

    def recordEvent(self):
        self.events.append(self.time)