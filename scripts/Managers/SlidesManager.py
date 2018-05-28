import bpy

class Slides(object):

    def __init__(self, gestionSlide, slidePos):
        self.gestionSlide = gestionSlide
        self.camera = bpy.ops.object.camera_add(location = (slidePos*20,5,0), rotation = (90,0,0))
        self.transitionDone = False
        self.actionDone = False
        self.listObjects = []

    def getListObjects(self):
        return self.listObjects

    def addObject(self, obj):
        self.listObjects.append(obj)

    def removeObject(self, obj):
        for i in range(0, len(self.listObjects) - 1):
            if self.listObjects[i] == obj:
                del self.listObjects[i]

    def updateObjects(self):
        pass

    def _getid(self):
        return self.gestionSlide.listSlides.index(self)

    def startTransition(self):

        """TODO"""

        self.transitionDone = True

    def startAction(self):

        """TODO"""

        self.actionDone = True

    def next(self):
        if self.transitionDone and self.actionDone:
            self.gestionSlide.setActiveSlide(self._getid()+1)
            bpy.context.scene.camera = self.gestionSlide.listSlides[self._getid()+1].camera


class SlidesManager(object):

    class __GestionSlides(object):

        def __init__(self):

            self.nbSlides = 0
            self.activeSlide = 0
            self.listSlides = []

        def addSlide(self):
            #self.listSlides.insert(Slides(self, self.activeSlide), self.activeSlide)
            self.listSlides.append(Slides(self, self.activeSlide))
            self.setActiveSlide(self.nbSlides)
            self.addNbSlide()

        def getNbSlides(self):
            return self.nbSlides

        def addNbSlide(self):
            self.nbSlides += 1

        def subNbSlide(self):
            self.nbSlides -= 1

        def getActiveSlide(self):
            return self.activeSlide

        def setActiveSlide(self, value):
            if value < len(self.listSlides):
                self.activeSlide = value - 1

        def removeSlide(self):
            for i in range(self.activeSlide + 1, len(self.listSlides) - 1):
                self.listSlides[i].camera.location[i] -= 20
            del self.listSlides[self.activeSlide]


    instance = None

    def __new__(cls):
        if SlidesManager.instance is None:
            SlidesManager.instance = SlidesManager.__GestionSlides()
        return SlidesManager.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
