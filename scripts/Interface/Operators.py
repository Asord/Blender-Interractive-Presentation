from bpy import types
from Slides import GestionSlides

# Abstract operator skeleton
class Operator(types.Operator):

    @classmethod
    def poll(cls, context):
        return context.object is not None


class OperatorAddSlide(Operator):

    bl_idname = "execution.add_slide"
    bl_label = "Add Slide"

    def invoke(self, context, event):
        gestSlide = GestionSlides()
        gestSlide.addSlide()
        return {'RUNNING_MODAL'}


class OperatorRemoveSlide(Operator):

    bl_idname = "execution.remove_slide"
    bl_label = "Remove Slide"

    def invoke(self, context, event):
        gestSlide = GestionSlides()
        gestSlide.removeSlide()
        return {'RUNNING_MODAL'}