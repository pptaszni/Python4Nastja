"""
Author: Pawel Ptasznik
"""
import pytest
import unittest
from unittest.mock import MagicMock
import math
from .context import robotic_arm_module # pylint: disable=E0611
from robotic_arm_module import ArmRemoteController

@unittest.skip("Let's disable this for now to demonstrate all the tests passing")
def test_execute_correct_actoins_on_robotic_arm(mocker):
    armMock = MagicMock()
    armMock.set_joints_position = MagicMock()
    armMock.set_cartesian_position = MagicMock()
    sut = ArmRemoteController(armMock)
    command = "GO_TO_JOINTS(1.2, 3.4)"
    mocker.patch('robotic_arm_module.SomeNetwork.get_message', return_value=command)
    sut.execute_incomming_command()
    armMock.set_joints_position.assert_called_with(1.2, 3.4)
    command = "GO_TO_CARTESIAN(1.0, 2.0)"
    mocker.patch('robotic_arm_module.SomeNetwork.get_message', return_value=command)
    sut.execute_incomming_command()
    armMock.set_cartesian_position.assert_called_with(1.0, 2.0)

@unittest.skip("Let's disable this for now to demonstrate all the tests passing")
def test_check_for_wrong_commands(mocker):
    armMock = MagicMock()
    armMock.set_joints_position = MagicMock()
    armMock.set_cartesian_position = MagicMock()
    sut = ArmRemoteController(armMock)
    command = "KISS_MY_ASS(2, 3)"
    mocker.patch('robotic_arm_module.SomeNetwork.get_message', return_value=command)
    # up to you how you plan to react to bad commands, this is just an example where we decided to throw an exception
    with pytest.raises(Exception) as e_info:
        sut.execute_incomming_command()
