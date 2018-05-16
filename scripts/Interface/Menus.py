from . import Operators
from bpy import types, ops
from Managers.XMLParser import XMLNodes

# Abstract menu skeleton
class Menu(types.Panel):

    bl_category    = XMLNodes[1]["Category"]
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    bl_label = "" # override variable

    def __init__(self):
        types.Panel.__init__(self)

        self.split = self.layout.split()

        self.row = self.layout.row()
        self.col = self.split.column()

class MenuMain(Menu):

    bl_label = XMLNodes[1]["MainMenu"]

    def draw(self, context):
        self.col.operator(Operators.OperatorCameraView.bl_idname, text=XMLNodes[0]["Camera"])


class MenuSlide(Menu):

    bl_label = XMLNodes[1]["Slide"]

    def draw(self, context):

        self.col.prop(context.scene.prop_nb_slides, "Active_Slide")
        
        self.col.operator(Operators.OperatorAddSlide.bl_idname,    text=XMLNodes[0]["AddSlide"])
        self.col.operator(Operators.OperatorRemoveSlide.bl_idname, text=XMLNodes[0]["RemoveSlide"])
        


class MenuAnimation(Menu):

    bl_label = XMLNodes[1]["Animation"]

    def draw(self, context):
      
        self.col.operator(Operators.OperatorAddAnim.bl_idname, text=XMLNodes[1]["AddAnim"])
        #self.col.operator("mesh.primitive_cube_add", text = "Remove a slide")

        #self.row.label(text = "Remove a slide")
