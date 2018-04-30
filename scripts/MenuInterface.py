from Interface import *
from bpy import utils


classes = (
    PropNumberSlide,

    OperatorAddSlide,
    OperatorCameraView,

    MenuGeneral,
    MenuSlides,
    MenuAnimation,
)

def register():
    for cl in classes:
        utils.register_class(cl)

    registerProps()

def unregister():
    for cl in classes:
        utils.unregister_class(cl)


if __name__ == "__main__":
    register()



