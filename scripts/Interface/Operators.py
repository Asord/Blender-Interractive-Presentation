from bpy import types, ops

# Abstract operator skeleton
class Operator(types.Operator):

    @classmethod
    def poll(cls, context):
        return context.object is not None


class OperatorAddSlide(Operator):

    bl_idname = "operator.add_slide"
    bl_label = "Add Slide"

    def invoke(self, context, event):
        """ TODO: Code pour ajouter les slides """
        return {'RUNNING_MODAL'}

class OperatorCameraView(Operator):
    bl_idname = "operator.camera_view"
    bl_label = "Camera view"

    def invoke(self, context, event):
        ops.view3d.viewnumpad(type='CAMERA')
        return {'RUNNING_MODAL'}