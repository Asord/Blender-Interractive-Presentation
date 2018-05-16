from Interface import *
import Slides
from bpy import utils, types, props


classes = (
    PropNumberSlide,
    OperatorAddSlide,
    OperatorRemoveSlide,

    MenuSlides,
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


if __name__ == "__main__":
    register()



