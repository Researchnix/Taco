import abc

class CarRouteGen:
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def __getRoute__(self):
        raise NotImplementedError('route generation must be implemented!')