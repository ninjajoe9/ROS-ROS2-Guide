#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_recieve_message_data(msg):
    rospy.loginfo("Message recieved: ")
    rospy.loginfo(msg)

if __name__ == "__main__":
    rospy.init_node('example_subscriber')

    sub = rospy.Subscriber("/example_topic", String, callback_recieve_message_data)

    rospy.spin()
