from . import Operators
from bpy import types

# Abstract menu skeleton
class Menu(types.Panel):

    bl_category = "Presentation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    bl_label = "" # override variable

    def __init__(self):
        types.Panel.__init__(self)

        self.split = self.layout.split()

        self.row = self.layout.row()
        self.col = self.split.column()


class MenuSlides(Menu):

    bl_label = "Slides"

    def draw(self, context):

        """self.row.label(text = "Slide")"""

        self.col.prop(context.scene.prop_nb_slides, "Active_Slide")

        self.col.operator(Operators.OperatorAddSlide.bl_idname, text ="Add a slide")
        self.col.operator(Operators.OperatorRemoveSlide.bl_idname, text = "Remove a slide")


class MenuAnimation(Menu):

    bl_label = "Animation"

    def draw(self, context):

        self.col.operator("mesh.primitive_cube_add", text = "Add a slide")
        self.col.operator("mesh.primitive_cube_add", text = "Remove a slide")
