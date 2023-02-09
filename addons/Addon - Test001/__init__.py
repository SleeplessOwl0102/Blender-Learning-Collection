bl_info = {
    "name": "Move X Axis",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import addon_utils
class ObjectMoveX(bpy.types.Operator):
    """Ren Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.move_xss"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Move X by One"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)

def register():
    bpy.utils.register_class(ObjectMoveX)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

    print(addon_utils.paths())

def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

    # Removes the new operator from an existing menu.
    # 不加的话开发时会重复注册
    bpy.types.VIEW3D_MT_object.remove(menu_func)

