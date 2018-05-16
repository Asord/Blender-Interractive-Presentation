from bpy import types, ops
from Managers.XMLParser import XMLNodes

# Abstract operator skeleton
class Operator(types.Operator):

    @classmethod
    def poll(cls, context):
        return context.object is not None

class OperatorAddSlide(Operator):

    bl_idname = "operator.add_slide"
    bl_label = XMLNodes[1]["AddSlide"]
    bl_description = XMLNodes[3]["AddSlideDesc"]

    def invoke(self, context, event):
        """ TODO: Code pour ajouter les slides """
        return {'RUNNING_MODAL'}

class OperatorRemoveSlide(Operator):

    bl_idname = "operator.remove_slide"
    bl_label = XMLNodes[1]["RemoveSlide"]
    bl_description = XMLNodes[3]["RemoveSlideDesc"]

    def invoke(self, context, event):
        """ TODO: Code pour ajouter les slides """
        return {'RUNNING_MODAL'}

class OperatorCameraView(Operator):
    bl_idname = "operator.camera_view"
    bl_label = XMLNodes[1]["Camera"]
    bl_description = XMLNodes[3]["CameraDesc"]

    def invoke(self, context, event):
        ops.view3d.viewnumpad(type='CAMERA')
        return {'RUNNING_MODAL'}

class OperatorAddAnim(Operator):
    bl_idname = "operator.add_animation"
    bl_label = XMLNodes[1]["AddAnim"]
    bl_description = XMLNodes[3]["AddAnimDesc"]

    def invoke(self, context, event):
        ops.view3d.viewnumpad(type='CAMERA')
        return {'RUNNING_MODAL'}