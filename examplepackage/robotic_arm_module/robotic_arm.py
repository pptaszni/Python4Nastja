"""
Author: Pawel Ptasznik
"""

"""
This class models 2 DOF robotic arm. By convention when q1==0 and q2==0 robotic arm lies on the X axis of cartesian plane. Arm rotates counter clokwise given positive coordinates until PI.
Length from first joint so second joint = 4
Length from second joint to the efector = 3
"""
class Arm2DOF:
    def __init__(self):
        self.__q1__ = 0.0
        self.__q2__ = 0.0
        self.__L1__ = 4.0
        self.__L2__ = 3.0
    def get_joints_coordinates(self):
        return (self.__q1__, self.__q2__)
    def get_cartesian_coordinates(self):
        return (0.0, 0.0)
    def set_joints_position(self, q1, q2):
        pass
    def set_cartesian_position(self, x, y):
        pass

