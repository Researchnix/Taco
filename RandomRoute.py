
import Map


from random import randint


class RandomRoute():
    graph = Map

    def __init__(self, graph):
        self.graph = graph

    def __getRoute__(self, length):
        visited = {}
        route = []
        skeylist = self.graph.streets.keys()
        first = self.graph.streets[skeylist[randint(0, len(skeylist)-1)]]
        route.append(first.ID)
        current = first.toID
        for i in range(length):
            visited[current.ID] = True
            for j in range(len(current.outgoing)):
                if not visited.get(current.outgoing[j].toID, False):
                    route.append(current.outgoing[j].ID)
                    current = self.graph.intersections[current.outgoing[j].toID]
                    break
        return route
