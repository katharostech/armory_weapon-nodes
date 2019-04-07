
import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class WeaponShotDelay(Node, ArmLogicTreeNode):
    '''Shot Delay Node'''
    bl_idname = 'LNWeaponShotDelay'
    bl_label = 'Shot Delay'
    #bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketFloat', 'Delay')
        self.outputs.new('ArmNodeSocketAction', 'Out')

add_node(WeaponShotDelay, category='Weapon')
