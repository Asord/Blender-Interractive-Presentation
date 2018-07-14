"""
Script that run the presentation
To be activated once
"""
# Append the project directory to Blender modules path
from sys import path
path.append(".")


from bge import logic, events
from Models.Singloton import singleton

scene = logic.getCurrentScene()

@singleton
class runManager:

    """
    runManager that run the presentation

    :var listSlides: the list of all slides
    :type listSlides: Slides[]
    :var camera: the camera of the presentation
    :type camera: Blender Camera Game Object
    :var pos: the slide current position
    :type pos: int
    """

    def __init__(self):

        self.listSlides = []
        self.camera = None
        self.pos = 0
        self.startSort()
        self.sortObjects()


    def startSort(self):
        """
        #TODO: description
        """
        for i in range(1, len(scene.objects) + 1):
            temp = []
            for j in range(len(scene.objects)):
                if scene.objects[j].name[0:6] == "Slide{}".format(i):
                        temp.append(scene.objects[j])

                elif scene.objects[j].name == "cam":
                    scene.objects[j].worldPosition = [0.0, 5.0, 0.0]
                    self.camera = scene.objects[j]

                else:
                    if scene.objects[j].name[0:5] != "Slide":
                        scene.objects[j].worldPosition  = [-1.0, 0.0, 0.0]

            if temp:
                self.listSlides.append(temp)

    def sortObjects(self):
        """
        #TODO: description
        """
        temp = []
        for slide in self.listSlides:
            for obj in slide:
                for j in range(len(slide) - 1):
                    if slide[j].name[7] > slide[j+1].name[7]:
                        slide[j], slide[j+1] = slide[j+1], slide[j]

            slide.append("transition{}".format(str(self.listSlides.index(slide) + 1)))
            temp += slide
        self.listSlides = temp

        temp = []
        for a in self.listSlides:
            if type(a) != str:
                if a.actuators:
                    self.startState(a)
                    temp.append(a)
            else:
                temp.append(a)
        self.listSlides = temp

    def nextPos(self):
        """
        TODO: desc
        TODO : Slide de fin
        TODO: VAL: pourquoi self.pos est utilisé comme un tableau et non un int ?
        """
        if self.pos[0:10] == "transition":
            self.pos = "Slide{}-1".format(int(self.pos[10]) + 1)

        elif int(self.pos[7]) == len(self.listSlides[int(self.pos[5])]):
            self.pos = "transition{}".format(int(self.pos[5]))

        else:
            self.pos = "Slide{}-{}".format(self.pos[5], str(int(self.pos[7]) + 1))

    def prevPos(self):
        """
        TODO: desc
        """
        if self.pos != 0:
            if self.pos[7] == "1":
                self.pos = "Slide{}-{}".format(int(self.pos[5]) - 1, len(self.listSlides[int(self.pos[5]) - 1]))
            else:
                self.pos = "Slide{}-{}".format(self.pos[5], str(int(self.pos[7]) - 1))

            for obj in scene.objects:
                if obj.name[0:8] == self.pos:
                    self.startState(obj)

    def startState(self, obj):
        """
        TODO: Desc

        :param obj: Blender GameObject
        :type obj: Blender GameObject
        """
        cont = obj.controllers[-1]
        act = cont.actuators[0]

        if act.name == "flash":
            obj.setVisible(False)

        if act.name == "motion":
            temp = ""
            pos1 = 0
            pos2 = 0
            for i in range(16, len(obj.name)-1):
                if obj.name[i] != ",":
                    temp+= obj.name[i]
                else:
                    pos1 = i + 1
                    break
            posX = float(temp)

            temp = ""
            for i in range(pos1, len(obj.name)-1):
                if obj.name[i] != ",":
                    temp+= obj.name[i]
                else:
                    pos2 = i + 1
                    break
            posY = float(temp)

            temp = ""
            for i in range(pos2, len(obj.name)-1):
                temp += obj.name[i]
            posZ = float(temp)

            obj.worldPosition = [posX, posY, posZ]
            obj.setVisible(False)



def next():
    """
    Simple method that go to the next position of the presentation
    """
    manager = runManager()

    keyboard = logic.keyboard
    JUST_ACTIVATED = logic.KX_INPUT_JUST_ACTIVATED
    if keyboard.events[events.RIGHTARROWKEY] == JUST_ACTIVATED:
        cont = scene.objects["cam"].controllers[-1]

        if type(manager.listSlides[manager.pos]) != str:
            act = cont.actuators[manager.listSlides[manager.pos].name[0:8]]
            cont.activate(act)

        else:
            actuator1 = cont.actuators["transition"]
            actuator2 = cont.actuators["limitTransition"]
            cont.activate(actuator2)
            cont.activate(actuator1)
            actuator2.max += 20

        manager.pos += 1

    if keyboard.events[events.LEFTARROWKEY] == JUST_ACTIVATED:
        cont = scene.objects["cam"].controllers[-1]

        manager.pos -= 1

        if type(manager.listSlides[manager.pos]) != str:
            print('ReState')
            manager.startState(manager.listSlides[manager.pos])
        else:
            manager.camera.worldPosition = [manager.camera.worldPosition[0] - 20, 5, 0]
            actuator2 = cont.actuators["limitTransition"]
            actuator2.max -= 20

def anim():
    """
    Simple function that start animations of objects
    """
    cont = logic.getCurrentController()

    if cont.actuators[0].name == "flash":
        act1 = cont.actuators[0]
        act2 = cont.actuators[1]
        cont.activate(act1)
        cont.activate(act2)

    if cont.actuators[0].name == "motion":
        own = cont.owner
        own.setVisible(True)
        act1 = cont.actuators[0]
        act2 = cont.actuators[1]
        act3 = cont.actuators[2]
        act4 = cont.actuators[3]
        cont.activate(act1)
        cont.activate(act2)
        cont.activate(act3)
        cont.activate(act4)

    if cont.actuators[0].name == "action":
        act1 = cont.actuators[0]
        cont.activate(act1)
