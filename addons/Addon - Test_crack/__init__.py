bl_info = {
    "name" : "破损与裂缝",
    "author" : "LaiYuxiang",
    "description" : "只需单击一次即可在Edge或Face中创建损坏或裂缝",
    "blender" : (3, 0, 0),
    "version" : (1, 1, 0),
    "category" : "3D View"
}

import bpy
import bpy.utils.previews
import os

def string_to_int(value):
    if value.isdigit():
        return int(value)
    return 0

def string_to_icon(value):
    if value in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys():
        return bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items[value].value
    return string_to_int(value)


def icon_to_string(value):
    for icon in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items:
        if icon.value == value:
            return icon.name
    return "NONE"

def enum_set_to_string(value):
    if type(value) == set:
        if len(value) > 0:
            return "[" + (", ").join(list(value)) + "]"
        return "[]"
    return value

def string_to_type(value, to_type, default):
    try:
        value = to_type(value)
    except:
        value = default
    return value

addon_keymaps = {}
_icons = None
cracks_and_damage_maker = {}

def property_exists(prop_path):
    try:
        eval(prop_path)
        return True
    except:
        return False
def sna_update_sna_damage__8A609(self, context):
    sna_updated_prop = self.sna_damage_
    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'node up11.blend') + r'\NodeTree', filename=sna_updated_prop, link=False)
    modifier_7EE75 = bpy.context.active_object.modifiers.new(name=sna_updated_prop, type='NODES', )
    bpy.context.active_object.modifiers.active.node_group = bpy.data.node_groups[sna_updated_prop]
    for i_95C67 in range(len(bpy.context.view_layer.objects.selected)):
        if bpy.context.view_layer.objects.selected[i_95C67].select_get():
            bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[i_95C67]
        else:
            pass
_item_map = dict()
def make_enum_item(_id, name, descr, preview_id, uid):
    lookup = str(_id)+"\0"+str(name)+"\0"+str(descr)+"\0"+str(preview_id)+"\0"+str(uid)
    if not lookup in _item_map:
        _item_map[lookup] = (_id, name, descr, preview_id, uid)
    return _item_map[lookup]
def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id

class SNA_PT_CRACKS_AND_DAMAGE_MAKER_C30E5(bpy.types.Panel):
    bl_label = 'Cracks And Damage Maker'
    bl_idname = 'SNA_PT_CRACKS_AND_DAMAGE_MAKER_C30E5'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'CD'
    bl_order = 0


    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout.template_icon_view(bpy.context.scene, 'sna_damage_', show_labels=False, scale=5.0, scale_popup=5.0)
        if property_exists("bpy.context.object.modifiers['edged']"):
            col_99D4D = layout.column(heading='', align=False)
            col_99D4D.alert = False
            col_99D4D.enabled = True
            col_99D4D.use_property_split = False
            col_99D4D.use_property_decorate = False
            col_99D4D.scale_x = 1.0
            col_99D4D.scale_y = 1.0
            col_99D4D.alignment = 'Expand'.upper()
            col_99D4D.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Subdivision Surface'].inputs[1], 'default_value', text='Sub Level S1', icon_value=0, emboss=True)
            col_99D4D.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Subdivide Mesh'].inputs[1], 'default_value', text='Sub Level S2', icon_value=0, emboss=True)
            col_99D4D.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Subdivision Surface'].inputs[2], 'default_value', text='Edge Crease', icon_value=0, emboss=True)
            col_99D4D.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Math'].inputs[1], 'default_value', text='Edge Hight', icon_value=0, emboss=True)
            col_99D4D.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Noise Texture'].inputs[1], 'default_value', text='Random 1', icon_value=0, emboss=True)
            col_99D4D.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Noise Texture'].inputs[5], 'default_value', text='Random 2', icon_value=0, emboss=True)
        else:
            col_07262 = layout.column(heading='', align=False)
            col_07262.alert = False
            col_07262.enabled = True
            col_07262.use_property_split = False
            col_07262.use_property_decorate = False
            col_07262.scale_x = 1.0
            col_07262.scale_y = 1.0
            col_07262.alignment = 'Expand'.upper()
            col_07262.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Subdivision Surface'].inputs[1], 'default_value', text='Sub Level S1', icon_value=0, emboss=True)
            col_07262.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Subdivide Mesh'].inputs[1], 'default_value', text='Sub Level S2', icon_value=0, emboss=True)
            col_07262.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Subdivision Surface'].inputs[2], 'default_value', text='Edge Crease', icon_value=0, emboss=True)
            col_07262.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Math'].inputs[1], 'default_value', text='Edge Hight', icon_value=0, emboss=True)
            col_07262.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Math'].inputs[1], 'default_value', text='R1', icon_value=0, emboss=True)
            col_07262.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Math.001'].inputs[1], 'default_value', text='R2', icon_value=0, emboss=True)
            col_07262.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Noise Texture'].inputs[1], 'default_value', text='R3', icon_value=0, emboss=True)

        layout.prop(bpy.context.active_object.modifiers.active.node_group.nodes['Set Material'].inputs[2], 'default_value', text='Material', icon_value=127, emboss=True)
def sna_damage__enum_items(self, context):
    enum_items = [['fe', 'fe', '', load_preview_icon(os.path.join(os.path.dirname(__file__), 'assets', 'i1.png'))], ['edged', 'edged', '', load_preview_icon(os.path.join(os.path.dirname(__file__),
                                                                                                                                                                          'assets', 'i2.png'))]]
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]



def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_damage_ = bpy.props.EnumProperty(name='Damage ', description='', items=sna_damage__enum_items, update=sna_update_sna_damage__8A609)

    bpy.utils.register_class(SNA_PT_CRACKS_AND_DAMAGE_MAKER_C30E5)

def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_damage_

    bpy.utils.unregister_class(SNA_PT_CRACKS_AND_DAMAGE_MAKER_C30E5)

