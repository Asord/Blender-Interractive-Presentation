from bpy import types, ops
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

class OperatorAddAnim(Operator):
    bl_idname = "operator.add_animation"
    bl_label = XMLData["label@AddAnim"]
    bl_description = XMLData["desc@AddAnimDesc"]

    def invoke(self, context, event):
        ops.view3d.viewnumpad(type='CAMERA')

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