from abc import abstractmethod, ABCMeta

class Animation(object, metaclass=ABCMeta):

    def __init__(self, duration):
        self._time = 0
        self._duration = duration

    @abstractmethod
    def Start(self):
        pass # TODO: déterminer l'utilisé avec __Animate

    @abstractmethod
    def Stop(self):
        pass

    @abstractmethod
    def Serialize(self):
        pass