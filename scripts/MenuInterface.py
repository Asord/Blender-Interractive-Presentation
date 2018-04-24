from Interface import *
from bpy import utils, types, props


classes = (
    PropNumberSlide,
    OperatorAddSlide,

    MenuSlides,
    MenuAnimation,
)

def register():
    for cl in classes:
        utils.register_class(cl)

    types.Scene.prop_nb_slides = props.PointerProperty(type=PropNumberSlide)

def unregister():
    for cl in classes:
        utils.unregister_class(cl)


if __name__ == "__main__":
    register()



