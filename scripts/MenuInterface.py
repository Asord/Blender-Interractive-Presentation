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
        self.col.prop(context.scene.customp, "size")

class MenuAnimation(MenuInterface):

    bl_label = "Animation"

    def draw(self, context):

        self.row.label(text = "Add slides")

        self.col.operator("mesh.primitive_cube_add", text = "Add a slide")
        self.col.operator("mesh.primitive_cube_add", text = "Remove a slide")

        self.row.label(text = "Remove a slide")


classes = (
    addon_Properties,
    AddSlide,
    MenuAnimation,
    MenuSlides
)

def register():
    for cl in classes:
        bpy.utils.register_class(cl)
    bpy.types.Scene.customp = bpy.props.PointerProperty(type=addon_Properties)

def unregister():
    for cl in classes:
        bpy.utils.unregister_class(cl)


if __name__ == "__main__":
    register()



