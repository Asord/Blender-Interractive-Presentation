from bpy import context, ops, data
from Models.Singloton import singleton
from Managers.AnimationManager import AnimationManager



class Slides(object):
    """
    Slides: class that contain all slides related contents

    :param gestionSlide: SlidesManager singloton reference
    :type gestionSlide: SlidesManager
    :param slidePos: Position of the slide
    :type slidePos: int

    Class variables:

    :var gestionSlide: the SlidesManager singloton
    :type gestionSlide: SlidesManager | __SlidesManager
    :var cameraPos: the base camera position of the slide
    :type cameraPos: Position[x, y, z]
    :var listObjects: the list of all Blender Objects linked to the slide
    :type listObjects: list[BlenderObjects]
    :var startMotion: the position where the motion will start
    :type startMotion: list[x, y, z]
    :var endMotion: the position where the motion will end
    :type endPosition: list[x, y, z]
    """
    def __init__(self, gestionSlide, slidePos):

        self.gestionSlide = gestionSlide
        self.cameraPos = [slidePos*20,5,0]
        self.listObjects = []
        #self.listAnimation = [] deparcted
        self.startMotion = [0.0, 0.0, 0.0]
        self.endMotion = [0.0, 0.0, 0.0]

    def addObject(self, obj):
        """
        Add an object to the slide

        :param obj: the object to add
        :type obj: BlenderObject
        """
        if obj.name[0:5]!= "Slide":
            self.listObjects.append(obj)
            self.renameObject(obj, self.gestionSlide.posActiveSlide + 1, len(self.listObjects))
            context.scene.objects.active = obj
            ops.logic.sensor_add(type = 'MESSAGE')
            context.scene.objects.active = self.gestionSlide.camera
            actuators = context.object.game.actuators
            ops.logic.actuator_add(type = 'MESSAGE')
            actuator = actuators[-1]
            actuator.name = obj.name
            actuator.to_property = obj.name
            controllers = context.object.game.controllers
            controller = controllers[-1]
            controller.link(None, actuator)
            context.scene.objects.active = obj

    def renameObject(self, obj, nSlide, nObj):
        """
        rename an object on the slide

        :param obj: the object to rename
        :type obj: BlenderObject
        :param nSlide: the number of the slide where the object is
        :type nSlide: int | None
        :param nObj: the number of objects in the slide
        :type nObj: int
        """
        if nSlide is None:
            nSlide = obj.name[5]

        if nObj is None:
            nObj = obj.name[7]

        obj.name = "Slide{}-{}".format(nSlide, nObj)

    def removeObject(self, obj):
        """
        Remove the object to the slide

        :param obj: the object to remove
        """
        ops.logic.sensor_remove(sensor=context.active_object.game.sensors[0].name, object=context.active_object.name)
        controllers = context.object.game.controllers
        if controllers:
            if controllers[0].actuators[0].name == "flash":
                self.removeAnimation("delFlash")
            elif controllers[0].actuators[0].name == "motion":
                self.removeAnimation("delMotion")
        ops.logic.actuator_remove(actuator=obj.name[0:8], object="cam")


        for i in range(self.listObjects.index(obj) + 1, len(self.listObjects)):
            self.renameObject(self.listObjects[i], None, int(self.listObjects[i].name[7]) - 1)
        self.listObjects.remove(obj)
        obj.name = "Object"

    def addAnimation(self, anim):
        """
        add an animation to a selected object

        :param anim: type of animation to set
        :type anim: Animation
        """
        for obj in self.listObjects:
            if obj == context.active_object:
                if anim == "flash":
                    self.gestionSlide.camera.game.actuators[obj.name].to_property = obj.name + "-flash"
                    obj.name += "-flash"
                    AnimationManager.animation(anim)

                if anim == "startMotion":
                    self.startMotion = obj.location.copy()

                if anim == "endMotion":
                    self.endMotion = obj.location.copy()

                if anim == "motion":

                    minStartMotionX = "% 5.2f" % self.startMotion[0]
                    minStartMotionY = "% 5.2f" % self.startMotion[1]
                    minStartMotionZ = "% 5.2f" % self.startMotion[2]

                    self.gestionSlide.camera.game.actuators[obj.name].to_property = obj.name + "-motion({},{},{})".format(minStartMotionX, minStartMotionY, minStartMotionZ)
                    obj.name += "-motion({},{},{})".format(minStartMotionX, minStartMotionY, minStartMotionZ)
                    AnimationManager.animation(anim, self.startMotion, self.endMotion)

                if anim == "cancelMotion":
                    self.startMotion = [0.0, 0.0, 0.0]
                    self.endMotion = [0.0, 0.0, 0.0]

    def removeAnimation(self, anim):
        """
        remove an animation to the selected object

        :param anim: the animation to remove
        """
        print('Etape 3', context.active_object.name)
        for obj in self.listObjects:
            if obj == context.active_object:
                print('Etape 4')
                if anim == "delFlash":
                    print('Etape 5')
                    obj.name = obj.name[0:8]
                    self.gestionSlide.camera.game.actuators[obj.name].to_property = obj.name
                    AnimationManager.animation(anim)
                if anim == "delMotion":
                    obj.name = obj.name[0:8]
                    self.gestionSlide.camera.game.actuators[obj.name].to_property = obj.name
                    AnimationManager.animation(anim)

    def __del__(self):
        """
        destructor that call destructor of all objects contained within the slide
        """
        ops.object.select_all(action='DESELECT')
        for obj in self.listObjects:
            obj.select = True
            ops.object.delete()
        del self


@singleton
class SlidesManager:
    """
    Singloton manager of all slides

    :var nbSlides: the number of slides
    :type nbSlides: int
    :var posActiveSlide: the active slide position
    :type posActiveSlide: int
    :var listSlides: the list of all Slides
    :type  listSlides: Slides[]
    :var camera: the camera object
    :type camera: Blender Camera Game Object
    :var isCameraView: boolean if the camera is the actual scene view
    :type isCameraView: bool
    """
    def __init__(self):

        self.nbSlides = 0
        self.posActiveSlide = -1
        self.listSlides = []
        self.camera = None
        self.isCameraView = False

    def addSlide(self):
        """
        add a slide to the slidesManager (and to the presentation)
        """
        if self.nbSlides == 0:
            self.listSlides.append(Slides(self,0))
            ops.object.camera_add(location=self.listSlides[0].cameraPos, rotation= (1.5708, 0, 0)) #Angle euler
            context.active_object.name = 'cam'
            self.camera = data.objects["cam"]

            sensors = context.object.game.sensors
            controllers = context.object.game.controllers
            actuators = context.object.game.actuators
            ops.logic.sensor_add(type='ALWAYS')
            sensor = sensors[-1]
            sensor.use_pulse_true_level = True
            ops.logic.controller_add(type='PYTHON')
            controller = controllers[-1]
            controller.mode = 'MODULE'
            controller.module = "run.next"
            ops.logic.actuator_add(type='MOTION')
            actuator1 = actuators[-1]
            actuator1.name = "transition"
            actuator1.offset_location[0] = 0.2
            ops.logic.actuator_add(type='CONSTRAINT')
            actuator2 = actuators[-1]
            actuator2.name = "limitTransition"
            actuator2.limit = 'LOCX'
            actuator2.limit_max = 0
            controller.link(sensor, actuator1)
            controller.link(None, actuator2)

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
                        self.listSlides[i].renameObject(obj, int(obj.name[5]) + 1, None)

        context.scene.prop_nb_slides['Active_Slide'] = self.posActiveSlide + 2
        self.posActiveSlide += 1

        self.addNbSlide()

    def getNbSlides(self):
        """
        Getter: get the number of slides
        """
        return self.nbSlides

    def addNbSlide(self):
        self.nbSlides += 1

    def subNbSlide(self):
        self.nbSlides -= 1

    def getActiveSlide(self):
        """
        :return: the active slide ID
        """
        return self.posActiveSlide

    def setActiveSlide(self, value):
        """
        set the active slide to a given value

        :param value: the slide ID to switch to
        :type value: int
        :return:
        """
        if value <= len(self.listSlides):
            self.posActiveSlide = value - 1
            self.camera.location = self.listSlides[self.posActiveSlide].cameraPos
            ops.object.select_all(action='DESELECT')
            self.camera.select = True
            ops.view3d.snap_cursor_to_active()
            context.space_data.cursor_location[1] = 30

    def removeSlide(self):
        """
        remove the current slide from the presentation
        """
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
                    self.listSlides[i].renameObject(obj, int(obj.name[5]) - 1, None)

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
