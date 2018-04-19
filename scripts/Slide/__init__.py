class Slide(object):

    numberOfSlides = 0

    def __init__(self, identifier):
        self._id = identifier
        self._preview = ""
        self._object = ""
        self._animation = None
        self._baseX = 0

    def Delete(self):
        pass # TODO: compléter

    def StartAnimation(self):
        if self._animation is not None:
            self._animation.Start()


    """ Getters / Setters """
    def GetPreview(self):
        pass # TODO: compléter

    def SetPreview(self, string):
        pass # TODO: compléter


    def GetObject(self):
        return self._object

    def SetObject(self, obj):
        self._object = obj

    def EditObject(self, **kwargs):
        pass # TODO: compléter

    def GetAnimation(self):
        return self._animation

    def SetAnimation(self, animation):
        self._animation = animation


    def GetID(self):
        return self._id


    def Serialize(self):
        pass # TODO: compléter

    def Show(self):
        pass # TODO: compléter
