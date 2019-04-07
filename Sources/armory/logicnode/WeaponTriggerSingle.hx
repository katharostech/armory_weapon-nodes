package armory.logicnode;

import haxe.ds.HashMap;


class WeaponTriggerSingle extends LogicNode {

	var hasShot:Bool = false;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run(from:Int) {
		if (from == 0) { // Trigger is Down
			if (hasShot == false) {
				runOutput(0);
				hasShot = true;
			}
		} else if (from == 1)  { // Trigger is Up
			if (hasShot == true) {
				hasShot = false;
			}
		}
	}
}
