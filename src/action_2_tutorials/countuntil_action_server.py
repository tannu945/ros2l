import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import time

from action_2_tutorials.action import CountUntil


class CountuntilActionServer(Node):

    def __init__(self):
        super().__init__('countuntil_action_server')
        self._action_server = ActionServer(
            self,
            CountUntil,
            'countuntil',
            self.execute_callback)
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = CountUntil.Feedback()
        counter = 0
        for i in range(0, goal_handle.request.max_number+1):
            feedback_msg.percentage = (i/goal_handle.request.max_number)*100
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.percentage))
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info('Waiting for {0} seconds.'.format(goal_handle.request.wait_duration))
            time.sleep(goal_handle.request.wait_duration)
            counter += 1


        goal_handle.succeed()

        result = CountUntil.Result()
        result.count = counter-1
        return result


def main(args=None):
    rclpy.init(args=args)

    countuntil_action_server = CountuntilActionServer()

    rclpy.spin(countuntil_action_server)


if __name__ == '__main__':
    main()