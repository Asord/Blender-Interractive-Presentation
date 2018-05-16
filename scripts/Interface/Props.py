from bpy import types, props, context
from Managers.XMLParser import XMLNodes

#abstract property skeleton
class Property(types.PropertyGroup):
    pass


class PropNumberSlide(Property):

    size = props.IntProperty(
            name = XMLNodes[2]["SlideSize"],
            description = XMLNodes[3]["SlideSizeDesc"],
            default = 1, max=10, min=0
    )

def registerProps():
    types.Scene.prop_nb_slides = props.PointerProperty(type=PropNumberSlide)