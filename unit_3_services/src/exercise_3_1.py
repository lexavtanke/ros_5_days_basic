#! /usr/bin/env python

import rospy
import rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest


# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client to be running
rospy.wait_for_service('/execute_trajectory')
execute_service_client = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
execute_request_obj = ExecTrajRequest()
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj_file_path = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

execute_request_obj.file = traj_file_path
result = execute_service_client(execute_request_obj)
print result