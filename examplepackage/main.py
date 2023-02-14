#!/usr/bin/env python

"""
Just a small example how we might use the code from our subpackages in production

Author: Pawel Ptasznik
"""

from robotic_arm_module import Arm2DOF
from robotic_arm_module import ArmRemoteController

if __name__ == "__main__":
    arm = Arm2DOF()
    ctrl = ArmRemoteController(arm)
    ctrl.execute_incomming_command()
