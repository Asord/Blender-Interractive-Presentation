from . import Operators
from bpy import types

from Managers.XMLParser import XMLData

# Abstract menu skeleton
class Menu(types.Panel):
    """
    Abstract class of all menu subcategories

    Must contain:

    :type bl_label: str @override
    :type draw(self, context): method @override
    """
    bl_category    = XMLData["label@Category"]
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    bl_label = "" # override variable

    def __init__(self):
        types.Panel.__init__(self)

        self.split = self.layout.split()

        self.row = self.layout.row()
        self.col = self.split.column()

    def draw(self, context):
        """
        :param context: the context where the element has to be drawed
        """
        pass

class MenuMain(Menu):

    bl_label = XMLData["label@MainMenu"]

    def draw(self, context):
        self.col.operator(Operators.OperatorCameraView.bl_idname, text=XMLData["button@Camera"])


class MenuSlide(Menu):

    bl_label = XMLData["label@Slide"]

    def draw(self, context):

        self.col.prop(context.scene.prop_nb_slides, "Active_Slide")
        
        self.col.operator(Operators.OperatorAddSlide.bl_idname,    text=XMLData["button@AddSlide"])
        self.col.operator(Operators.OperatorRemoveSlide.bl_idname, text=XMLData["button@RemoveSlide"])


class MenuAnimation(Menu):

    bl_label = XMLData["label@Animation"]

    def draw(self, context):

        if not context.scene.prop_custom_motion['is_Enable']:
            self.col.operator(Operators.OperatorFlash.bl_idname, text=XMLData["button@Flash"])
            self.col.operator(Operators.OperatorMotion.bl_idname, text=XMLData["button@Motion"])
            self.col.operator(Operators.OperatorRemoveAnimation.bl_idname, text=XMLData["button@RemoveAnimation"])

        if context.scene.prop_custom_motion['is_Enable']:
            self.col.operator(Operators.OperatorDefStartMotion.bl_idname, text=XMLData["button@DefStartMotion"])
            self.col.operator(Operators.OperatorDefEndMotion.bl_idname, text=XMLData["button@DefEndMotion"])
            self.col.operator(Operators.OperatorValidateMotion.bl_idname, text=XMLData["button@ValidateMotion"])
            self.col.operator(Operators.OperatorCancelMotion.bl_idname, text=XMLData["button@CancelMotion"])


class MenuObjet(Menu):

    bl_label = XMLData["label@Objects"]

    def draw(self, context):

        self.col.operator(Operators.OperatorLinkObject.bl_idname, text =XMLData["label@LinkObject"])
        self.col.operator(Operators.OperatorUnlinkObject.bl_idname, text =XMLData["label@UnlinkObject"])
