from abc import abstractmethod, ABCMeta

class Scene(object, metaclass=ABCMeta):

    @abstractmethod
    def Show(self):
        pass

    @abstractmethod
    def Hide(self):
        pass