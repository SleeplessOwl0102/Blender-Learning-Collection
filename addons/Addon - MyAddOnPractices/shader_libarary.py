import bpy

# Create a Custom Operator for the Diamond Shader
class SHADER_OT_DIAMOND(bpy.types.Operator):
    """Add the Diamond Shader to your selected Object."""
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator'

    def execute(self, context):
        # Creating a New Shader and calling it Diamond
        material_diamond = bpy.data.materials.new(name="Diamond")
        # Enabling Use Nodes
        material_diamond.use_nodes = True
        # removing the Principled Node
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        # Create a reference to the Material Output
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        # Set location of node
        material_output.location = (400, 0)

        # Adding Glass1 Node
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # Set location of node
        glass1_node.location = (-600, 0)
        # Setting the Default Color
        glass1_node.inputs[0].default_value = (1, 0, 0, 1)
        # Setting the Default IOR Value
        glass1_node.inputs[2].default_value = 1.446

        # Adding Glass2 Node
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # Set location of node
        glass2_node.location = (-600, -150)
        # Setting the Default Color
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)
        # Setting the Default IOR Value
        glass2_node.inputs[2].default_value = 1.450

        # Adding Glass3 Node
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # Set location of node
        glass3_node.location = (-600, -300)
        # Setting the Default Color
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        # Setting the Default IOR Value
        glass3_node.inputs[2].default_value = 1.545

        # Create the Add Shader Node and Reference it as 'Add1'
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        # Setting the Location
        add1_node.location = (-400, -50)
        # Setting the Label
        add1_node.label = "Add 1"
        # Minimizes the Node
        add1_node.hide = True
        # Deselect the Node
        add1_node.select = False

        # Create the Add Shader Node and Reference it as 'Add2'
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        # Setting the Location
        add2_node.location = (-100, 0)
        # Setting the Label
        add2_node.label = "Add 2"
        # Minimizes the Node
        add2_node.hide = True
        # Deselect the Node
        add2_node.select = False

        # Create the Glass Node and Reference it as 'glass4'
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # Setting the Location
        glass4_node.location = (-150, -150)
        # Setting the default color
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)
        # Setting the default IOR
        glass4_node.inputs[2].default_value = 1.450
        # Deselect the Node
        glass4_node.select = False

        # Create the Mix Shader Node and Reference it as 'Mix1'
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        # Setting the Location
        mix1_node.location = (200, 0)
        # Deselect the Node
        mix1_node.select = False

        # Creating Links between the Nodes
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])

        # Adding Material to the currently selected object
        bpy.context.object.active_material = material_diamond

        return {'FINISHED'}

    # Operator for the Gold (basic) Shader

class SHADER_OT_GOLD(bpy.types.Operator):
    """Add the Basic Gold Shader to your selected Object."""
    bl_label = "Gold"
    bl_idname = 'shader.gold_operator'

    def execute(self, context):
        # Create a Shader Material and name it Gold
        material_gold = bpy.data.materials.new(name="Gold")
        # Use Nodes for this Material
        material_gold.use_nodes = True

        # Create reference to the Material Output
        material_output = material_gold.node_tree.nodes.get('Material Output')
        material_output.location = (600, 0)
        material_output.select = False

        # Create the RGB Node and Reference it as 'rgb_node'
        rgb_node = material_gold.node_tree.nodes.new('ShaderNodeRGB')
        # Setting the Location
        rgb_node.location = (0, -100)
        # Setting the default color
        rgb_node.outputs[0].default_value = (1, 0.766, 0.336, 1)
        # Deselect the Node
        rgb_node.select = False
        # Minimize the Node
        rgb_node.hide = True

        # Create reference to the Principled Node
        principled = material_gold.node_tree.nodes.get('Principled BSDF')
        principled.location = (200, 0)
        principled.select = False
        principled.inputs[4].default_value = 1.0

        # Connecting (known as creating links) between the
        material_gold.node_tree.links.new(rgb_node.outputs[0], principled.inputs[0])

        # Adding Material to the currently selected object
        bpy.context.object.active_material = material_gold

        return {'FINISHED'}

    # Operator for the Silver (basic) Shader


class SHADER_OT_SILVER(bpy.types.Operator):
    """Add the Basic Silver Shader to your selected Object."""
    bl_label = "Silver"
    bl_idname = 'shader.silver_operator'

    def execute(self, context):
        # Create a Shader Material and name it Silver
        material_silver = bpy.data.materials.new(name="Silver")
        # Use Nodes for this Material
        material_silver.use_nodes = True

        # Create reference to the Material Output
        material_output = material_silver.node_tree.nodes.get('Material Output')
        material_output.location = (600, 0)
        material_output.select = False

        # Create the RGB Node and Reference it as 'rgb_node'
        rgb_node = material_silver.node_tree.nodes.new('ShaderNodeRGB')
        # Setting the Location
        rgb_node.location = (0, -100)
        # Setting the default color
        rgb_node.outputs[0].default_value = (0.972, 0.960, 0.915, 1)
        # Deselect the Node
        rgb_node.select = False
        # Minimize the Node
        rgb_node.hide = True

        # Create reference to the Principled Node
        principled = material_silver.node_tree.nodes.get('Principled BSDF')
        principled.location = (200, 0)
        principled.select = False
        principled.inputs[4].default_value = 1.0

        # Connecting (known as creating links) between the
        material_silver.node_tree.links.new(rgb_node.outputs[0], principled.inputs[0])

        # Adding Material to the currently selected object
        bpy.context.object.active_material = material_silver

        return {'FINISHED'}

    # Operator for the Copper (basic) Shader


class SHADER_OT_COPPER(bpy.types.Operator):
    """Add the Basic Copper Shader to your selected Object."""
    bl_label = "Copper"
    bl_idname = 'shader.copper_operator'

    def execute(self, context):
        # Create a Shader Material and name it Copper
        material_copper = bpy.data.materials.new(name="Copper")
        # Use Nodes for this Material
        material_copper.use_nodes = True

        # Create reference to the Material Output
        material_output = material_copper.node_tree.nodes.get('Material Output')
        material_output.location = (600, 0)
        material_output.select = False

        # Create the RGB Node and Reference it as 'rgb_node'
        rgb_node = material_copper.node_tree.nodes.new('ShaderNodeRGB')
        # Setting the Location
        rgb_node.location = (0, -100)
        # Setting the default color
        rgb_node.outputs[0].default_value = (0.955, 0.637, 0.538, 1)
        # Deselect the Node
        rgb_node.select = False
        # Minimize the Node
        rgb_node.hide = True

        # Create reference to the Principled Node
        principled = material_copper.node_tree.nodes.get('Principled BSDF')
        principled.location = (200, 0)
        principled.select = False
        principled.inputs[4].default_value = 1.0

        # Connecting (known as creating links) between the
        material_copper.node_tree.links.new(rgb_node.outputs[0], principled.inputs[0])

        # Adding Material to the currently selected object
        bpy.context.object.active_material = material_copper

        return {'FINISHED'}

    # Operator for the Ghost Shader


class SHADER_OT_GHOST(bpy.types.Operator):
    """Add the Ghost Shader to your selected Object."""
    bl_label = "Ghost"
    bl_idname = 'shader.ghost_operator'

    def execute(self, context):
        # Create a Shader Material and name it Ghost
        material_ghost = bpy.data.materials.new(name="Ghost")
        # Use Nodes for this Material
        material_ghost.use_nodes = True

        # Create reference to the Material Output
        material_output = material_ghost.node_tree.nodes.get('Material Output')
        material_output.location = (1000, 0)
        material_output.select = False

        # Select and remove the default Principled Node
        material_ghost.node_tree.nodes.remove(material_ghost.node_tree.nodes.get('Principled BSDF'))

        # Create the Emission Node and Reference it as 'emiss_node'
        emiss_node = material_ghost.node_tree.nodes.new('ShaderNodeEmission')
        # Setting the Location
        emiss_node.location = (-200, -90)
        # Setting the default color
        emiss_node.inputs[0].default_value = (0.224322, 0.812741, 1, 1)
        emiss_node.inputs[1].default_value = 2

        # Deselect the Node
        emiss_node.select = False

        # Create the Transparent Node and Reference it as 'trans_node'
        trans_node = material_ghost.node_tree.nodes.new('ShaderNodeBsdfTransparent')
        # Setting the Location
        trans_node.location = (-200, 10)
        # Setting the default color
        trans_node.inputs[0].default_value = (0.137478, 0.345533, 1, 1)
        # Deselect the Node
        trans_node.select = False

        # Create the Mix Node and Reference it as 'mix_node'
        mix_node = material_ghost.node_tree.nodes.new('ShaderNodeMixShader')
        # Setting the Location
        mix_node.location = (400, 50)
        # Deselect the Node
        mix_node.select = False

        # Create the Layer Weight Node and Reference it as 'layerw_node'
        layerw_node = material_ghost.node_tree.nodes.new('ShaderNodeLayerWeight')
        # Setting the Location
        layerw_node.location = (0, 150)
        # Setting the default color
        layerw_node.inputs[0].default_value = 0.1
        # Deselect the Node
        layerw_node.select = False

        # Create the Math Node and Reference it as 'math_node'
        math_node = material_ghost.node_tree.nodes.new('ShaderNodeMath')
        # Setting the Location
        math_node.location = (200, 100)
        # Setting the default color
        math_node.inputs[0].default_value = 0.1
        # Deselect the Node
        math_node.select = False
        math_node.hide = True

        # Create the Mix2 Node and Reference it as 'mix2_node'
        mix2_node = material_ghost.node_tree.nodes.new('ShaderNodeMixShader')
        # Setting the Location
        mix2_node.location = (800, 50)
        # Deselect the Node
        mix2_node.select = False

        # Create the Transparent2 Node and Reference it as 'trans2_node'
        trans2_node = material_ghost.node_tree.nodes.new('ShaderNodeBsdfTransparent')
        # Setting the Location
        trans2_node.location = (500, -100)
        # Setting the default color
        trans2_node.inputs[0].default_value = (1, 1, 1, 1)
        # Deselect the Node
        trans2_node.select = False

        # Create the LightPath Node and Reference it as 'light_node'
        light_node = material_ghost.node_tree.nodes.new('ShaderNodeLightPath')
        # Setting the Location
        light_node.location = (500, 500)
        # Deselect the Node
        light_node.select = False

        # Connecting (known as creating links) between the
        material_ghost.node_tree.links.new(trans_node.outputs[0], mix_node.inputs[1])
        material_ghost.node_tree.links.new(emiss_node.outputs[0], mix_node.inputs[2])
        material_ghost.node_tree.links.new(layerw_node.outputs[0], math_node.inputs[0])
        material_ghost.node_tree.links.new(layerw_node.outputs[1], math_node.inputs[1])
        material_ghost.node_tree.links.new(math_node.outputs[0], mix_node.inputs[0])
        material_ghost.node_tree.links.new(mix_node.outputs[0], mix2_node.inputs[1])
        material_ghost.node_tree.links.new(trans2_node.outputs[0], mix2_node.inputs[2])
        material_ghost.node_tree.links.new(light_node.outputs[11], mix2_node.inputs[0])
        material_ghost.node_tree.links.new(mix2_node.outputs[0], material_output.inputs[0])

        # Adding Material to the currently selected object
        bpy.context.object.active_material = material_ghost

        return {'FINISHED'}

    # Operator for the Hologram Shader


class SHADER_OT_HOLOGRAM(bpy.types.Operator):
    """Add the Hologram Shader to your selected Object."""
    bl_label = "Hologram"
    bl_idname = 'shader.hologram_operator'

    def execute(self, context):
        # Create a Shader Material and name it Ghost
        material_hologram = bpy.data.materials.new(name="Hologram")
        # Use Nodes for this Material
        material_hologram.use_nodes = True

        # Create reference to the Material Output
        material_output = material_hologram.node_tree.nodes.get('Material Output')
        material_output.location = (1000, 0)
        material_output.select = False

        # Select and remove the default Principled Node
        material_hologram.node_tree.nodes.remove(material_hologram.node_tree.nodes.get('Principled BSDF'))

        # Create the Emission Node and Reference it as 'emiss_node'
        emiss_node = material_hologram.node_tree.nodes.new('ShaderNodeEmission')
        # Setting the Location
        emiss_node.location = (-200, -90)
        # Setting the default color
        emiss_node.inputs[0].default_value = (0.0927682, 1, 0.566671, 1)
        # Setting the Strength Value
        emiss_node.inputs[1].default_value = 2
        # Deselect the Node
        emiss_node.select = False

        # Create the Transparent Node and Reference it as 'trans1_node'
        trans1_node = material_hologram.node_tree.nodes.new('ShaderNodeBsdfTransparent')
        # Setting the Location
        trans1_node.location = (-200, 10)
        # Setting the default color
        trans1_node.inputs[0].default_value = (0.381055, 1, 0.697353, 1)
        # Deselect the Node
        trans1_node.select = False

        # Create the Mix1 Node and Reference it as 'mix1_node'
        mix1_node = material_hologram.node_tree.nodes.new('ShaderNodeMixShader')
        # Setting the Location
        mix1_node.location = (400, 50)
        # Deselect the Node
        mix1_node.select = False

        # Create the Layer Weight Node and Reference it as 'layerw_node'
        layerw_node = material_hologram.node_tree.nodes.new('ShaderNodeLayerWeight')
        # Setting the Location
        layerw_node.location = (0, 150)
        # Setting the default color
        layerw_node.inputs[0].default_value = 0.1
        # Deselect the Node
        layerw_node.select = False

        # Create the Math Node and Reference it as 'math_node'
        math_node = material_hologram.node_tree.nodes.new('ShaderNodeMath')
        # Setting the Location
        math_node.location = (200, 100)
        # Setting the default color
        math_node.inputs[0].default_value = 0.1
        # Deselect the Node
        math_node.select = False
        math_node.hide = True

        # Create the Mix2 Node and Reference it as 'mix2_node'
        mix2_node = material_hologram.node_tree.nodes.new('ShaderNodeMixShader')
        # Setting the Location
        mix2_node.location = (600, 50)
        # Deselect the Node
        mix2_node.select = False

        # Create the Wireframe Node and Reference it as 'mix_node'
        wire_node = material_hologram.node_tree.nodes.new('ShaderNodeWireframe')
        # Setting the Location
        wire_node.location = (100, 200)
        # Deselect the Node
        wire_node.select = False
        # Enable Use Pixel Size
        wire_node.use_pixel_size = True
        # Enable Use Pixel Size
        wire_node.inputs[0].default_value = 0.05

        # create a reroute node
        reroute = material_hologram.node_tree.nodes.new('NodeReroute')
        reroute.location = (-150, -90)

        # Connecting (known as creating links) between the
        material_hologram.node_tree.links.new(trans1_node.outputs[0], mix1_node.inputs[1])
        material_hologram.node_tree.links.new(emiss_node.outputs[0], reroute.inputs[0])
        material_hologram.node_tree.links.new(reroute.outputs[0], mix1_node.inputs[2])
        material_hologram.node_tree.links.new(reroute.outputs[0], mix2_node.inputs[2])
        material_hologram.node_tree.links.new(layerw_node.outputs[0], math_node.inputs[0])
        material_hologram.node_tree.links.new(layerw_node.outputs[1], math_node.inputs[1])
        material_hologram.node_tree.links.new(math_node.outputs[0], mix1_node.inputs[0])
        material_hologram.node_tree.links.new(mix1_node.outputs[0], mix2_node.inputs[1])
        material_hologram.node_tree.links.new(wire_node.outputs[0], mix2_node.inputs[0])

        material_hologram.node_tree.links.new(mix2_node.outputs[0], material_output.inputs[0])

        # Adding Material to the currently selected object
        bpy.context.object.active_material = material_hologram

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SHADER_OT_DIAMOND)
    bpy.utils.register_class(SHADER_OT_GOLD)
    bpy.utils.register_class(SHADER_OT_SILVER)
    bpy.utils.register_class(SHADER_OT_COPPER)
    bpy.utils.register_class(SHADER_OT_GHOST)
    bpy.utils.register_class(SHADER_OT_HOLOGRAM)

def unregister():
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    bpy.utils.unregister_class(SHADER_OT_GOLD)
    bpy.utils.unregister_class(SHADER_OT_SILVER)
    bpy.utils.unregister_class(SHADER_OT_COPPER)
    bpy.utils.unregister_class(SHADER_OT_GHOST)
    bpy.utils.unregister_class(SHADER_OT_HOLOGRAM)