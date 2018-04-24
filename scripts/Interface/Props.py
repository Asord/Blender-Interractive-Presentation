from bpy import types, props

#abstract property skeleton
class Property(types.PropertyGroup):
    pass


class PropNumberSlide(Property):

    size = props.IntProperty(
            name = "size",
            description = "size of the object to add",
            default = 1, max=10, min=0
    )