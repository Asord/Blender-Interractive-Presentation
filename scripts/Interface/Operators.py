from bpy import types, ops, data
from Managers.SlidesManager import SlidesManager

from Managers.XMLParser import XMLData

# Abstract operator skeleton
class Operator(types.Operator):
    """
    Abstract class of all menu subcategories

    Must contain:

    :type bl_idname: str @override
    :type bl_label: str @override
    :type bl_description: str @override
    :type invoke(self, context, event): method @override
    """
    bl_idname = ""
    bl_label = ""
    bl_description = ""

    @classmethod
    def poll(cls, context):
        """
        Method related to a Blender fonctionnality (check if operator exists)

        :param context: the context where the element exists
        :return: bool
        """
        return context.object is not None

    def invoke(self, context, event):
        """
        Method related to Blender fonctionnality (called when the button is pressed)

        :param context: the context which contain the operator
        :type context: blender.context
        :param event: the event who activate the operator
        :type event: blender.event
        :return: {str}
        """
        pass

class OperatorAddSlide(Operator):
    bl_idname = "operator.add_slide"
    bl_label = XMLData["button@AddSlide"]
    bl_description = XMLData["desc@AddSlideDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        gestSlide.addSlide()
        return {'RUNNING_MODAL'}

class OperatorRemoveSlide(Operator):

    bl_idname = "operator.remove_slide"
    bl_label = XMLData["button@RemoveSlide"]
    bl_description = XMLData["desc@RemoveSlideDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        listSize = len(gestSlide.listSlides[gestSlide.posActiveSlide].listObjects)
        if listSize == 0:
            gestSlide.removeSlide()
        else:
            ops.operator.popupdelete('INVOKE_DEFAULT')
        return {'RUNNING_MODAL'}

class OperatorCameraView(Operator):
    bl_idname = "operator.camera_view"
    bl_label = XMLData["button@Camera"]
    bl_description = XMLData["desc@CameraDesc"]

    def invoke(self, context, event):
        ops.view3d.viewnumpad(type='CAMERA')
        return {'RUNNING_MODAL'}

class OperatorFlash(Operator):
    bl_idname = "operator.add_flash"
    bl_label = XMLData["button@Flash"]
    bl_description = XMLData["desc@AddFlashDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        gestSlide.listSlides[gestSlide.posActiveSlide].addAnimation('flash')
        return {'RUNNING_MODAL'}

class OperatorMotion(Operator):
    bl_idname = "operator.add_motion"
    bl_label = XMLData["button@Motion"]
    bl_description = XMLData["desc@MotionDesc"]

    def invoke(self, context, event):

        context.scene.prop_custom_motion['is_Enable'] = True

        return {'RUNNING_MODAL'}

class OperatorDefStartMotion(Operator):
    bl_idname = "operator.def_start"
    bl_label = XMLData["button@DefStartMotion"]
    bl_description = XMLData["desc@DefStartMotionDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        gestSlide.listSlides[gestSlide.posActiveSlide].addAnimation('startMotion')

        return {'RUNNING_MODAL'}

class OperatorDefEndMotion(Operator):
    bl_idname = "operator.def_end"
    bl_label = XMLData["button@DefEndtMotion"]
    bl_description = XMLData["desc@DefEndMotionDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        gestSlide.listSlides[gestSlide.posActiveSlide].addAnimation('endMotion')

        return {'RUNNING_MODAL'}

class OperatorValidateMotion(Operator):
    bl_idname = "operator.validate_motion"
    bl_label = XMLData["button@ValidateMotion"]
    bl_description = XMLData["desc@ValidateMotionDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        gestSlide.listSlides[gestSlide.posActiveSlide].addAnimation('motion')

        context.scene.prop_custom_motion['is_Enable'] = False

        return {'RUNNING_MODAL'}

class OperatorCancelMotion(Operator):
    bl_idname = "operator.cancel_motion"
    bl_label = XMLData["button@CancelMotion"]
    bl_description = XMLData["desc@CancelMotionDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        gestSlide.listSlides[gestSlide.posActiveSlide].addAnimation('cancelMotion')

        context.scene.prop_custom_motion['is_Enable'] = False

        return {'RUNNING_MODAL'}

class OperatorAction(Operator):
    bl_idname = "operator.add_action"
    bl_label = XMLData["button@Action"]
    bl_description = XMLData["desc@AddActionDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        gestSlide.listSlides[gestSlide.posActiveSlide].addAnimation('action')
        return {'RUNNING_MODAL'}

class OperatorRemoveAnimation(Operator):
    bl_idname = "operator.remove_animation"
    bl_label = XMLData["button@RemoveAnimation"]
    bl_description = XMLData["desc@RemoveAnimationDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        controllers = context.object.game.controllers
        if controllers:
            print('Etape 1')
            if controllers[0].actuators[0].name == "flash":
                print('Etape 2')
                gestSlide.listSlides[gestSlide.posActiveSlide].removeAnimation('delFlash')
            elif controllers[0].actuators[0].name == "motion":
                gestSlide.listSlides[gestSlide.posActiveSlide].removeAnimation('delMotion')
            elif controllers[0].actuators[0].name == "action":
                gestSlide.listSlides[gestSlide.posActiveSlide].removeAnimation('delAction')

        return {'RUNNING_MODAL'}

class OperatorLinkObject(Operator):
    bl_idname = "operator.link_object"
    bl_label = XMLData["label@LinkObject"]
    bl_description = XMLData["desc@LinkObjectDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        if gestSlide.nbSlides > 0:
            gestSlide.listSlides[gestSlide.posActiveSlide].addObject(context.active_object)
        return {'RUNNING_MODAL'}

class OperatorUnlinkObject(Operator):
    bl_idname = "operator.unlink_object"
    bl_label = XMLData["label@UnlinkObject"]
    bl_description = XMLData["desc@UnlinkObjectDesc"]

    def invoke(self, context, event):
        gestSlide = SlidesManager()
        if context.active_object.name[0:5] == "Slide":
            gestSlide.listSlides[gestSlide.posActiveSlide].removeObject(context.active_object)
        return {'RUNNING_MODAL'}

class PopupDeleteSlide(Operator):
    bl_idname = "operator.popupdelete"
    bl_label = XMLData["label@deleteSlideName"]
    bl_description = XMLData["desc@deleteSlideDesc"]

    def execute(self, context):
        gestSlide = SlidesManager()
        gestSlide.removeSlide()
        return {'INTERFACE'}

    def cancel(self, context):
        pass

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=250)

    def draw(self, context):
        for line in XMLData["popup@DeleteSlideMessage"].split('#'):
            self.layout.label(line)