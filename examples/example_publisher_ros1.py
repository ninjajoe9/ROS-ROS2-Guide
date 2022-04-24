#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":

    rospy.init_node('example_publisher')

    pub = rospy.Publisher("/example_topic", String, queue_size=10)
    rate = rospy.Rate(1)
    rospy.loginfo("Example publisher started")

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "This is a test message"
        pub.publish(msg)
        rate.sleep()
