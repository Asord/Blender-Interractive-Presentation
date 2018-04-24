from Interface import *

class AddSlide(Execution):

    bl_idname = "execution.add_slide"
    bl_label = "Add Slide"

    def invoke(self, context, event):
        """ TODO: Code pour ajouter les slides """
        return {'RUNNING_MODAL'}


class MenuSlides(MenuInterface):

    bl_label = "Slides"

    def draw(self, context):

        self.row.label(text = "Slides")

        self.layout.operator_context = 'INVOKE_DEFAULT'
        self.col.operator(AddSlide.bl_idname, text = "Add a slide")
        self.col.operator("mesh.primitive_cube_add", text = "Remove a slide")

class MenuAnimation(MenuInterface):

    bl_label = "Animation"

    def draw(self, context):

        self.row.label(text = "Add slides")

        self.col.operator("mesh.primitive_cube_add", text = "Add a slide")
        self.col.operator("mesh.primitive_cube_add", text = "Remove a slide")

        self.row.label(text = "Remove a slide")


def register():
    bpy.utils.register_class(AddSlide)
    bpy.utils.register_class(MenuAnimation)
    bpy.utils.register_class(MenuSlides)
def unregister():
    bpy.utils.unregister_class(AddSlide)
    bpy.utils.unregister_class(MenuAnimation)
    bpy.utils.unregister_class(MenuSlides)


if __name__ == "__main__":
    register()



