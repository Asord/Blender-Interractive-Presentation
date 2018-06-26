from Managers.XMLParser import init_XMLParser

init_XMLParser("texts.xml", "en-US", ["button", "label", "prop", "desc", "popup"])

from bpy import utils
from Interface import *
from Managers.SlidesManager import SlidesManager

class main:
    classes = (
        PropNumberSlide,

        OperatorCameraView,
        OperatorAddSlide,
        OperatorRemoveSlide,
        OperatorAddAnim,
        OperatorLinkObject,

        PopupDeleteSlide,

        MenuMain,
        MenuSlide,
        MenuAnimation,
        MenuObjet,
    )

    @staticmethod
    def register():
        """
        Register all Blender related classes contained inside the 'classes' container
        Also register all props from registerProps() contained inside Interface.Props file
        Create the first instance of SlidesManager singloton
        """
        for cl in main.classes:

            try:
                utils.register_class(cl)
            except ValueError:
                utils.unregister_class(cl)
                utils.register_class(cl)

        registerProps()

        SlidesManager()

    @staticmethod
    def unregister():
        """
        Unregister all Blender related classes contained inside the 'classes' container
        """
        for cl in main.classes:
            try:
                utils.unregister_class(cl)
            except RuntimeError:
                pass

if __name__ == "__main__":
    main.unregister()
    main.register()