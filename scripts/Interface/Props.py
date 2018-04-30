from bpy import types, props, context

#abstract property skeleton
class Property(types.PropertyGroup):
    pass


class PropNumberSlide(Property):

    size = props.IntProperty(
            name = "size",
            description = "size of the object to add",
            default = 1, max=10, min=0
    )

def registerProps():
    types.Scene.prop_nb_slides = props.PointerProperty(type=PropNumberSlide)