from Managers.XMLParser import *

XMLData = InitXMLParser("texts.xml")
lang = "en-US"
XMLNodes.append(NodeArray(XMLData, lang, "button"))
XMLNodes.append(NodeArray(XMLData, lang, "label"))
XMLNodes.append(NodeArray(XMLData, lang, "prop"))
XMLNodes.append(NodeArray(XMLData, lang, "desc"))

from Interface import *
import Slides
from bpy import utils, types, props


classes = (
    PropNumberSlide,

    OperatorCameraView,
    OperatorAddSlide,
    OperatorRemoveSlide,
    OperatorAddAnim,

    MenuMain,
    MenuSlide,
    MenuAnimation,
)

def register():
    for cl in classes:
        try:
            utils.register_class(cl)
        except ValueError:
            utils.unregister_class(cl)
            utils.register_class(cl)

    types.Scene.prop_nb_slides = props.PointerProperty(type=PropNumberSlide)
    
    Slides.GestionSlides()
    
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



