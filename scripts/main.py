# Append the project directory to Blender modules path
from sys import path
path.append(".")

# Import the XMLparser
from Managers.XMLParser import init_XMLParser, path

init_XMLParser(path("texts.xml"), "en-US", ["button", "label", "prop", "desc", "popup"])

# Import the bpy functions needed and all interface elements
from bpy import utils, context
from Interface import *

# Import the Slides Manager
from Managers.SlidesManager import SlidesManager

classes = (
    PropNumberSlide,
    PropCustomMotion,

    OperatorCameraView,
    OperatorAddSlide,
    OperatorRemoveSlide,
    OperatorFlash,
    OperatorMotion,
    OperatorDefStartMotion,
    OperatorDefEndMotion,
    OperatorValidateMotion,
    OperatorCancelMotion,
    OperatorAction,
    OperatorRemoveAnimation,
    OperatorUnlinkObject,
    OperatorLinkObject,

    PopupDeleteSlide,

    MenuMain,
    MenuSlide,
    MenuAnimation,
    MenuObjet
)

def register():
    """
    Register all Blender related classes contained inside the 'classes' container
    Also register all props from registerProps() contained inside Interface.Props file
    Create the first instance of SlidesManager singloton
    """

    for cl in classes:

        try:
            utils.register_class(cl)
        except ValueError:
            utils.unregister_class(cl)
            utils.register_class(cl)

    registerProps()

    context.scene.prop_custom_motion['is_Enable'] = False

    SlidesManager()

def unregister():
    """
    Unregister all Blender related classes contained inside the 'classes' container
    """
    for cl in classes:
        try:
            utils.unregister_class(cl)
        except RuntimeError:
            pass

if __name__ == "__main__":
    unregister()
    register()