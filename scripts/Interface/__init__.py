import bpy

class MenuInterface(bpy.types.Panel):

    bl_category = "Presentation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    bl_label = "" # override variable

    def __init__(self):
        bpy.types.Panel.__init__(self)

        self.split = self.layout.split()

        self.row = self.layout.row()
        self.col = self.split.column()


class Execution(bpy.types.Operator):

    @classmethod
    def poll(cls, context):
        return context.object is not None
