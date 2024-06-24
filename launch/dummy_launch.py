from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rtf_sensors',
            executable='rtf_imu',
            name='imu'
        ),
        # Node(
        #     package='rtf_lidar',
        #     executable='rtf_urg',
        #     name='lidar',
        #     # parameters=[
        #     #     {'turtlename': 'turtle1'}
        #     # ]
        # ),
    ])