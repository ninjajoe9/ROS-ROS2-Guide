#!/usr/bin/env python3

import rospy
from rospy_tutorials.srv import AddTwoInts

def handle_add_two_ints(request):
    result = request.a + request.b
    rospy.loginfo(str(request.a) + " + " + str(request.b) + " = " + str(result))
    return result

if __name__ == "__main__":
    rospy.init_node("add_two_int_server")
    service = rospy.Service("/add_two_ints", AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Add two ints server node started")

    rospy.spin()
