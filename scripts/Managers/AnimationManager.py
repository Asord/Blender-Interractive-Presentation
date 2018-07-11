from bpy import context, ops, data

class AnimationManager(object):
    """
    static class that define all basic animations

    To use it: call animation(animation name, [more args])

    contains:
    flash()
    delFlash()

    motion(start_point, end_point)
    delMotion()
    """

    @staticmethod
    def animation(item, *args):
        if item is "flash":
            AnimationManager.flash()
        if item is "motion":
            AnimationManager.motion(*args)
        if item is "delFlash":
            AnimationManager.delFlash()
        if item is "delMotion":
            AnimationManager.delMotion()

    @staticmethod
    def flash():
        sensors = context.object.game.sensors
        controllers = context.object.game.controllers
        actuators = context.object.game.actuators

        sensor = sensors[-1]

        ops.logic.controller_add(type='PYTHON')
        controller = controllers[-1]
        controller.name = "python"
        controller.mode = 'MODULE'
        controller.module = "run.anim"

        ops.logic.actuator_add(type='VISIBILITY')
        actuator1 = actuators[0]
        actuator1.name = "flash"
        actuator1.use_visible = True

        ops.logic.actuator_add(type='CONSTRAINT')
        actuator2 = actuators[1]
        actuator2.name = "constraint"

        controller.link(sensor, actuator1)
        controller.link(None, actuator2)

    @staticmethod
    def delFlash():
        ops.logic.controller_remove(controller = "python", object = context.active_object.name)
        ops.logic.actuator_remove(actuator = "flash", object = context.active_object.name)
        ops.logic.actuator_remove(actuator = "constraint", object = context.active_object.name)
        print('Etape finale')

    @staticmethod
    def motion(startLocation, endLocation):
        sensors = context.object.game.sensors
        controllers = context.object.game.controllers
        actuators = context.object.game.actuators

        sensor = sensors[-1]

        ops.logic.controller_add(type='PYTHON')
        controller = controllers[-1]
        controller.name = "python"
        controller.mode = 'MODULE'
        controller.module = "run.anim"

        ops.logic.actuator_add(type='MOTION')
        actuator1 = actuators[0]
        actuator1.name = "motion"

        ops.logic.actuator_add(type='CONSTRAINT')
        actuator2 = actuators[1]
        actuator2.name = "constraint1"
        actuator2.limit = 'LOCX'
        ops.logic.actuator_add(type='CONSTRAINT')
        actuator3 = actuators[2]
        actuator3.name = "constraint2"
        actuator3.limit = 'LOCY'
        ops.logic.actuator_add(type='CONSTRAINT')
        actuator4 = actuators[3]
        actuator4.name = "constraint3"
        actuator4.limit = 'LOCZ'

        if startLocation[0] < endLocation[0]:
            actuator1.offset_location[0] = 0.2
            actuator2.limit_min = -9999
            actuator2.limit_max = endLocation[0]
        elif startLocation[0] > endLocation[0]:
            actuator1.offset_location[0] = -0.2
            actuator2.limit_min = endLocation[0]
            actuator2.limit_max = 9999
        else:
            actuator1.offset_location[0] = 0.0
            actuator2.limit_min = -9999
            actuator2.limit_max = 9999

        if startLocation[1] < endLocation[1]:
            actuator1.offset_location[1] = 0.2
            actuator3.limit_min = -9999
            actuator3.limit_max = endLocation[1]
        elif startLocation[1] > endLocation[1]:
            actuator1.offset_location[1] = -0.2
            actuator3.limit_min = endLocation[1]
            actuator3.limit_max = 9999
        else:
            actuator1.offset_location[1] = 0.0
            actuator3.limit_min = -9999
            actuator3.limit_max = 9999

        if startLocation[2] < endLocation[2]:
            actuator1.offset_location[2] = 0.2
            actuator4.limit_min = -9999
            actuator4.limit_max = endLocation[2]
        elif startLocation[2] > endLocation[2]:
            actuator1.offset_location[2] = -0.2
            actuator4.limit_min = endLocation[2]
            actuator4.limit_max = 9999
        else:
            actuator1.offset_location[2] = 0.0
            actuator4.limit_min = -9999
            actuator4.limit_max = 9999



        controller.link(sensor, actuator1)
        controller.link(None, actuator2)
        controller.link(None, actuator3)
        controller.link(None, actuator4)

    @staticmethod
    def delMotion():
        ops.logic.controller_remove(controller = "python", object = context.active_object.name)
        ops.logic.actuator_remove(actuator = "motion", object = context.object.name)
        ops.logic.actuator_remove(actuator = "constraint1", object = context.object.name)
        ops.logic.actuator_remove(actuator = "constraint2", object = context.object.name)
        ops.logic.actuator_remove(actuator = "constraint3", object = context.object.name)

