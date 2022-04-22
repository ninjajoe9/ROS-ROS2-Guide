#!/usr/bin/env python3

import rospy

if __name__ == "__main__":
    counter = 0

    rospy.init_node('python_node')

    rospy.loginfo("start python node")


    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        counter += 1
        rospy.loginfo("Hello " + str(counter))
        rate.sleep()
