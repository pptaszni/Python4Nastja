"""
© Copyright CERN 2019.  All rights reserved. This software is released under a CERN proprietary
software licence. Any permission to use it shall be granted in writing. Requests shall be
addressed to CERN through mail-KT@cern.ch

Author: Pawel Ptasznik CERN EN/SMM/MRO
"""

from . import helpers

class RobotsStorage:
    def __init__(self, num_robots):
        if num_robots < 0:
            raise ValueError("Cannot construct RobotsStorage with negative int %d" % num_robots)
        self.__num_robots__ = num_robots
    def get_num_robots(self):
        return self.__num_robots__
    def add_robot(self):
        self.__num_robots__ += 1
        return True
    def remove_robot(self):
        if self.__num_robots__ == 0:
            return False
        self.__num_robots__ -= 1
        return True

# in this example names a b c x are actually OK, normally they are not
def quadratic_function_using_helper(a, b, c, x): # pylint: disable=invalid-name
    return helpers.square(a)*x + b*x + c
