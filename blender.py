import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *
import arm.nodes_logic
from logicnode_definitions import *

def register():
    arm.nodes_logic.register_nodes()

#def register():
    # Add custom nodes
    #add_node(WeaponShotDelay, category='AGES Weapons')
    #add_node(WeaponTriggerSingle, category='AGES Weapons')
    # Register newly added nodes
    #arm.nodes_logic.register_nodes()
