from bpy import types

# Abstract operator skeleton
class Operator(types.Operator):

    @classmethod
    def poll(cls, context):
        return context.object is not None


class OperatorAddSlide(Operator):

    bl_idname = "execution.add_slide"
    bl_label = "Add Slide"

    def invoke(self, context, event):
        """ TODO: Code pour ajouter les slides """
        return {'RUNNING_MODAL'}