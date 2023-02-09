bl_info = {
    "name": "MyAddObject",
    "author": "",
    "description": "",
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}
# 开启BlenderIcon viewer addon，点一下icon就会复制到剪贴板
import bpy


# This is the Main Panel (Parent of Panel A and B)
class MainPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'

    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2

        row = layout.row()
        row.label(text="Add an object", icon='OBJECT_ORIGIN')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon='CUBE', text="Cube")
        row.operator("mesh.primitive_uv_sphere_add", icon='SPHERE', text="Sphere")
        row.operator("mesh.primitive_monkey_add", icon='MESH_MONKEY', text="Suzanne")
        row = layout.row()
        row.operator("curve.primitive_bezier_curve_add", icon='CURVE_BEZCURVE', text="Bezier Curve")
        row.operator("curve.primitive_bezier_circle_add", icon='CURVE_BEZCIRCLE', text="Bezier Circle")

        row = layout.row()
        row.operator("object.text_add", icon='FILE_FONT', text="Add Font")
        row = layout.row()

    # This is Panel A - The Scale Sub Panel (Child of MainPanel)


class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.label(text="Select an option to scale your", icon='FONT_DATA')
        row = layout.row()
        row.label(text="      object.")
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        layout.scale_y = 1.2

        col = layout.column()
        col.prop(obj, "scale")

    # This is Panel B - The Specials Sub Panel (Child of MainPanel)


class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Select a Special Option", icon='COLOR_BLUE')
        row = layout.row()
        row.operator("object.shade_smooth", icon='MOD_SMOOTH', text="Set Smooth Shading")
        row.operator("object.subdivision_set", icon='MOD_SUBSURF', text="Add Subsurf")
        row = layout.row()
        row.operator("object.modifier_add", icon='MODIFIER')

    # Here we are Registering the Classes


def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)

    # Here we are UnRegistering the Classes


def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)

    # This is required in order for the script to run in the text editor


if __name__ == "__main__":
    register()
