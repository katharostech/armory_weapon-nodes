package armory.logicnode;

import iron.system.Time;


/**
 * A `LogicNode` designed to provide a shot delay for weapons. The node will
 * refuse to trigger its output until the delay time has passed.
 */
class WeaponShotDelay extends LogicNode {

	var lastShotTime:Float = 0.0;

	public function new(tree:LogicTree) {
		super(tree);
	}

	/**
	 * Run output only if the delay time since the last shot has passed.
	 */
	override function run(from:Int) {
		var shotDelay:Int = inputs[1].get();
		if (Time.time() - lastShotTime > shotDelay || lastShotTime == 0) {
			runOutput(0);
			lastShotTime = Time.time();
		}
	}
}
