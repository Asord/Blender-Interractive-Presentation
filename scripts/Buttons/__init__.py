from abc import abstractmethod, ABCMeta

class Button(object, metaclass=ABCMeta):

    @abstractmethod
    def Action(self, *args):
        pass

    @abstractmethod
    def Lock(self):
        pass #TODO: renomer la methode

    @abstractmethod
    def Unlock(self):
        pass #TODO: renomer la methode