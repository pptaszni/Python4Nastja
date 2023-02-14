"""
Author: Pawel Ptasznik
"""
import pytest
from unittest.mock import MagicMock
import math
from .context import robotic_arm_module # pylint: disable=E0611
from robotic_arm_module import ArmRemoteController

epsilon = 0.001



def test_execute_correct_actoins_on_robotic_arm(mocker):
    armMock = MagicMock()
    armMock.set_joints_position = MagicMock()
    sut = ArmRemoteController(armMock)
    command = "GO_TO_JOINTS(1.2, 3.4)"
    mocker.patch('robotic_arm_module.SomeNetwork.get_message', return_value=command)
    sut.execute_incomming_command()
    armMock.set_joints_position.assert_called_with(1.2, 3.4)
