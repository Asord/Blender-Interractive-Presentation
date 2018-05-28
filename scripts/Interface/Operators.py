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
        gestSlide.removeSlide()
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

class OperatorLinkObject(Operator):
    bl_idname = "operator.link_object"
    bl_label = "Link object"
    bl_description = """TODO"""

    def invoke(self, context, event):
        