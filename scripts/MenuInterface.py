from Managers.XMLParser import *

XMLData = InitXMLParser("texts.xml")
lang = "en-US"
XMLNodes.append(NodeArray(XMLData, lang, "button"))
XMLNodes.append(NodeArray(XMLData, lang, "label"))
XMLNodes.append(NodeArray(XMLData, lang, "prop"))
XMLNodes.append(NodeArray(XMLData, lang, "desc"))

from Interface import *
from bpy import utils


classes = (
    PropNumberSlide,

    OperatorAddSlide,
    OperatorCameraView,
    OperatorRemoveSlide,
    OperatorAddAnim,

    MenuMain,
    MenuSlide,
    MenuAnimation,
)

def register():
    for cl in classes:
        utils.register_class(cl)

    registerProps()

def unregister():
    for cl in classes:
        try:
            utils.unregister_class(cl)
        except RuntimeError as e:
            print(e)


if __name__ == "__main__":
    unregister()
    register()



