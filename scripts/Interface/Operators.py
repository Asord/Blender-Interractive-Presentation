from bpy import types, ops
from Slides import GestionSlides
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
        gestSlide = GestionSlides()
        gestSlide.addSlide()
        return {'RUNNING_MODAL'}

class OperatorRemoveSlide(Operator):

    bl_idname = "operator.remove_slide"
    bl_label = XMLNodes[1]["RemoveSlide"]
    bl_description = XMLNodes[3]["RemoveSlideDesc"]

    def invoke(self, context, event):
        gestSlide = GestionSlides()
        gestSlide.removeSlide()
        return {'RUNNING_MODAL'}

class OperatorCameraView(Operator):
    bl_idname = "operator.camera_view"
    bl_label = XMLNodes[1]["Camera"]
    bl_description = XMLNodes[3]["CameraDesc"]

    def invoke(self, context, event):
        if GestionSlides().nbSlides > 0:
            ops.view3d.viewnumpad(type='CAMERA')
            ops.object.select_all(action='DESELECT')
            GestionSlides().camera.select = True
            context.scene.objects.active = GestionSlides().camera
            ops.view3d.snap_cursor_to_active()
            context.space_data.cursor_location[1] = 30

            if GestionSlides().isCameraView:
                GestionSlides().isCameraView = False
            else:
                GestionSlides().isCameraView = True
                
        return {'RUNNING_MODAL'}

class OperatorAddAnim(Operator):
    bl_idname = "operator.add_animation"
    bl_label = XMLNodes[1]["AddAnim"]
    bl_description = XMLNodes[3]["AddAnimDesc"]

    def invoke(self, context, event):
        ops.view3d.viewnumpad(type='CAMERA')