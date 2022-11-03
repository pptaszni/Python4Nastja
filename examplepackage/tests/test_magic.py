"""
© Copyright CERN 2019.  All rights reserved. This software is released under a CERN proprietary
software licence. Any permission to use it shall be granted in writing. Requests shall be
addressed to CERN through mail-KT@cern.ch

Author: Pawel Ptasznik CERN EN/SMM/MRO
"""
import pytest
from .context import example_module # pylint: disable=E0611

def test_robots_storage_raises_exception_if_constructed_with_negative_arg(): # pylint: disable=invalid-name
    with pytest.raises(Exception):
        example_module.robotics_magic.RobotsStorage(-1)

def test_robots_storage_returns_correct_number_of_robots(): # pylint: disable=invalid-name
    storage = example_module.robotics_magic.RobotsStorage(69)
    assert storage.get_num_robots() == 69

def test_robots_storage_correctly_increment_decrement_number_of_robots(): # pylint: disable=invalid-name
    storage = example_module.robotics_magic.RobotsStorage(1)
    assert storage.add_robot()
    assert storage.get_num_robots() == 2
    assert storage.remove_robot()
    assert storage.remove_robot()
    assert not storage.remove_robot()
    assert storage.get_num_robots() == 0

def test_quadratic_function_returns_correct_result(): # pylint: disable=invalid-name
    fun = example_module.robotics_magic.quadratic_function_using_helper
    assert fun(1, 2, 3, 4) == 15
