

from Managers.XMLParser import init_XMLParser

init_XMLParser("texts.xml", "en-US", ["button", "label", "prop", "desc"])
from bpy import utils
from Interface import *
from Managers.SlidesManager import SlidesManager

classes = (
    PropNumberSlide,

    OperatorCameraView,
    OperatorAddSlide,
    OperatorRemoveSlide,
    OperatorAddAnim,
    OperatorLinkObject,

    MenuMain,
    MenuSlide,
    MenuAnimation,
    MenuObjet,
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

    SlidesManager()

def unregister():
    """
    Unregister all Blender related classes contained inside the "classes' container
    """
    for cl in classes:
        try:
            utils.unregister_class(cl)
        except RuntimeError:
            pass

if __name__ == "__main__":
    unregister()
    register()