import bpy

class MenuSlides(bpy.types.Panel):

    bl_category = "Presentation"
    bl_label = "Slides"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text = "Slides")

        split = layout.split()
        col = split.column()

        col.operator("mesh.primitive_cube_add", text = "Add a slide")
        col.operator("mesh.primitive_cube_add", text = "Remove a slide")

class MenuAnimation(bpy.types.Panel):

    bl_category = "Presentation"
    bl_label = "Animation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text = "Add slides")

        split = layout.split()
        col = split.column()

        col.operator("mesh.primitive_cube_add", text = "Add a slide")
        col.operator("mesh.primitive_cube_add", text = "Remove a slide")

        row = layout.row()
        row.label(text = "Remove a slide")


def register():
    bpy.utils.register_class(MenuAnimation)
    bpy.utils.register_class(MenuSlides)
def unregister():
    bpy.utils.unregister_class(MenuAnimation)
    bpy.utils.unregister_class(MenuSlides)


if __name__ == "__main__":
    register()



