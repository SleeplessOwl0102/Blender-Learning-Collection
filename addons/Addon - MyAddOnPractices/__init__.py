import random

bl_info = {
    "name": "s",
    "author": "",
    "description": "",
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

import bpy


# This is the Main Panel (Parent of Panel A and B)s
class MainPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.random_move_vertexs", text="Random Move Vertexs")
        row.operator("object.random_select_vertex_from_selection_vertex", text="随机选取顶点")


        obj = context.active_object
        vtx = obj.data.vertices
        vtx_count = len(vtx)
        converted_num = str(vtx_count)
        row = layout.row()
        row.label(text=converted_num, icon='OBJECT_DATA')


# This is Panel A - The Scale Sub Panel (Child of MainPanel)
class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    # 以下两个只需要定义一个
    # bl_category = 'Object Adder'
    bl_parent_id = 'PT_MainPanel'  # 设置父UI层级id，如果不设置会同在



    def draw(self, context):
        obj = context.active_object
        layout = self.layout
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        layout.scale_y = 1.2
        col = layout.column()
        col.prop(obj, "scale")

        row = layout.row()
        row.label(text="Select a Shader to be added.")

        row = layout.row()

        # 开启BlenderIcon viewer addon，点一下icon就会复制到剪贴板
        row.operator('shader.gold_operator', icon='KEYTYPE_KEYFRAME_VEC')
        row.operator('shader.silver_operator')
        row.operator('shader.copper_operator')

        row = layout.row()
        row.operator('shader.diamond_operator')
        row.operator('shader.ghost_operator')
        row.operator('shader.hologram_operator')


class RandomMoveSelectObjectVertex(bpy.types.Operator):
    """ 随机移动顶点 """
    bl_idname = "object.random_move_vertexs"
    bl_label = "Random Move Vertexs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        vtx = obj.data.vertices

        vtx_count = len(vtx)
        for i in range(vtx_count):
            vtx[i].co.x += random.uniform(-0.5, 0.5)
            vtx[i].co.y += random.uniform(-0.5, 0.5)
            vtx[i].co.z += random.uniform(-0.5, 0.5)
        return {'FINISHED'}

class RandomSelectVertexInEditMode(bpy.types.Operator):
    """随机选取顶点"""
    bl_idname = "object.random_select_vertex_from_selection_vertex"
    bl_label = "随机选取顶点"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        #check if in edit mode
        if bpy.context.mode != 'EDIT_MESH':
            return {'FINISHED'}
        #clear selection
        bpy.ops.mesh.select_all(action='DESELECT')
        #select random vertex
        bpy.ops.mesh.select_random( ratio=0.5, seed= random.randint(0, 1000))
        return {'FINISHED'}

# blender 没法用import，所以用from
from .shader_libarary import register, unregister
from .blender_manual import register, unregister

# When the add-on is enabled, Blender executes the code and runs the register() function.
def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(RandomMoveSelectObjectVertex)
    bpy.utils.register_class(RandomSelectVertexInEditMode)
    shader_libarary.register()
    blender_manual.register()

# When the add-on is disabled, Blender runs the unregister() function.
def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(RandomMoveSelectObjectVertex)
    bpy.utils.unregister_class(RandomSelectVertexInEditMode)
    shader_libarary.unregister()
    blender_manual.unregister()

