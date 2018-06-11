from bpy import context, ops, data
from BPL import Singloton, Debug
from Managers import AnimationManager



class Slides(object):

    def __init__(self, gestionSlide, slidePos):
        self.gestionSlide = gestionSlide
        self.cameraPos = [slidePos*20,5,0]
        self.transitionDone = True
        self.actionDone = True
        self.listObjects = []
        self.listAnimation = []
        self.pos = 0

    def addObject(self, obj):
        self.listObjects.append(obj)
        self.listAnimation.append(None)

    def removeObject(self, obj):
        self.listObjects.remove(obj)

    def addAnimation(self, anim):
        i = 0
        for obj in self.listObjects:
            if obj == context.active_object:
                self.listAnimation[i] = anim
                func = "AnimationManager.{}()".format(self.listAnimation[i])
                exec(func)
            i += 1


    def startTransition(self):

        """TODO"""

        self.transitionDone = True

    def startAction(self):

        """TODO"""

        self.actionDone = True

    def next(self):
        if len(self.listObjects) != 0:
            self.startTransition()
        elif self.pos == len(self.listObjects) - 1:
            if self.transitionDone and self.actionDone:
                print('NEXT')
        #else:


    def __del__(self):
        ops.object.select_all(action='DESELECT')
        for obj in self.listObjects:
            obj.select = True
            ops.object.delete()
        del self


class SlidesManager(Singloton):

    class __SlidesManager(object):

        def __init__(self):

            self.nbSlides = 0
            self.posActiveSlide = -1
            self.listSlides = []
            self.camera = None
            self.isCameraView = False

        def addSlide(self):
            if self.nbSlides == 0:
                self.listSlides.append(Slides(self,0))
                ops.object.camera_add(location=self.listSlides[0].cameraPos, rotation= (1.5708, 0, 0)) #Angle euler
                context.active_object.name = 'cam'
                self.camera = data.objects["cam"]

                sensors = context.object.game.sensors
                controllers = context.object.game.controllers
                ops.logic.sensor_add(type='ALWAYS')
                sensor = sensors[-1]
                sensor.use_pulse_true_level = True
                ops.logic.controller_add(type='PYTHON')
                controller = controllers[-1]
                controller.mode = 'SCRIPT'
                controller.text = data.texts["run.py"]
                sensor.link(controller)

            else:
                if self.posActiveSlide + 1 == self.nbSlides:
                    self.listSlides.append(Slides(self, self.nbSlides))
                    ops.object.select_all(action='DESELECT')
                    self.camera.select = True
                    self.camera.location = self.listSlides[self.nbSlides].cameraPos

                else:
                    self.listSlides.insert(self.posActiveSlide + 1, Slides(self, self.posActiveSlide + 1))
                    ops.object.select_all(action='DESELECT')
                    self.camera.select = True
                    self.camera.location = self.listSlides[self.posActiveSlide + 2].cameraPos
                    for i in range(self.posActiveSlide + 2, self.nbSlides + 1):
                        self.listSlides[i].cameraPos[0] += 20
                        for obj in self.listSlides[i].listObjects:
                            obj.location.x += 20
                            obj.name = "Object_Slide-{}".format(self.posActiveSlide + 2)

            context.scene.prop_nb_slides['Active_Slide'] = self.posActiveSlide + 2
            self.posActiveSlide += 1

            self.addNbSlide()


        def getNbSlides(self):
            return self.nbSlides

        def addNbSlide(self):
            self.nbSlides += 1

        def subNbSlide(self):
            self.nbSlides -= 1

        def getActiveSlide(self):
            return self.posActiveSlide

        def setActiveSlide(self, value):
            if value <= len(self.listSlides):
                self.posActiveSlide = value - 1
                self.camera.location = self.listSlides[self.posActiveSlide].cameraPos
                ops.object.select_all(action='DESELECT')
                self.camera.select = True
                ops.view3d.snap_cursor_to_active()
                context.space_data.cursor_location[1] = 30

        def removeSlide(self):
            if self.nbSlides == 1:
                ops.object.select_all(action='DESELECT')
                self.camera.select = True
                ops.object.delete()
                del self.listSlides[0]
                context.scene.prop_nb_slides['Active_Slide'] = 0
                self.posActiveSlide = -1

            else:
                for i in range(self.posActiveSlide + 1, len(self.listSlides)):
                    self.listSlides[i].cameraPos[0] -= 20
                    for obj in self.listSlides[i].listObjects:
                        obj.location.x -= 20
                        obj.name = "Object_Slide-{}".format(self.posActiveSlide + 1)

                del self.listSlides[self.posActiveSlide]

                if self.posActiveSlide != 0:
                    context.scene.prop_nb_slides['Active_Slide'] = self.posActiveSlide
                self.camera.location = self.listSlides[self.posActiveSlide - 1].cameraPos
                ops.object.select_all(action='DESELECT')
                self.camera.select = True

                if self.isCameraView:
                    context.space_data.cursor_location[0] -= 20

                if self.posActiveSlide !=0:
                    self.posActiveSlide -= 1

            self.subNbSlide()

    _ClassName = __SlidesManager