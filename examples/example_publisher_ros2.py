#!/urs/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class ExamplePublisher(Node):
    def __init__(self):
        super().__init__("example_publisher")

        self.publisher_ = self.create_publisher(String, "example_topic", 10)
        self.timer_ = self.create_timer(0.5, self.publish_message)
        self.get_logger().info("Example publisher started")

    def publish_news(self):
        msg = String()
        msg.data = "This is a test message"
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
