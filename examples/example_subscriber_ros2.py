#!/urs/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class ExampleSubscriber(Node):
    def __init__(self):
        super().__init__("example_subscriber")
        self.subscriber_ = self.create_subscription(String, "example_topic", self.callback_robot_news, 10)
        self.get_logger().info("Example subscriber started")

    def callback_robot_info(self, msg):
        self.get_logger().info("Message Recieved: ")
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ExampleSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
