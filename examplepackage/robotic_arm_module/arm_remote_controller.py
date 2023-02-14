"""
Author: Pawel Ptasznik
"""

"""
This class models some kind of communication point that listens to remote commands and executes them on the robotic arm
"""

"""
Example of not so great design. Our controller class is strongly coupled with some concrete implementation
of a network adapter. Any change of network communication directly impacts controller implementation.
"""
class SomeNetwork:
    def get_message(self):
        return "xxx"

class ArmRemoteController:
    def __init__(self, arm):
        self.__network__ = SomeNetwork()
        self.__arm__ = arm
    def execute_incomming_command(self):
        command = self.__network__.get_message()
        print("executing command: " + command)
        self.__arm__.set_joints_position(1.2, 3.4)
        # impl logic to execute arm movement based on the received message

"""
GO_TO_JOINTS(q1, q2)  --> arm.set_joints_position(q1, q2)
GO_TO_CARTESIAN(x, y) --> arm.set_cartesian_position(x, y)
"""
