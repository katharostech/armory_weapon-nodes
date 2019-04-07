
import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class WeaponTriggerSingle(Node, ArmLogicTreeNode):
    '''Trigger Single Node'''
    bl_idname = 'LNWeaponTriggerSingle'
    bl_label = 'Trigger Single'
    #bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'Trigger Down')
        self.inputs.new('ArmNodeSocketAction', 'Trigger Up')
        self.outputs.new('ArmNodeSocketAction', 'Out')

add_node(WeaponTriggerSingle, category='Weapon')
