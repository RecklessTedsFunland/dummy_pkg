from launch import LaunchDescription
from launch_ros.actions import Node
from rosbag2.launch_actions import Record


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rtf_sensors',
            executable='rtf_imu',
            name='imu'
        ),
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["0","0","0","0","0","0","world","laser"]
        ),
        Node(
            package='rtf_lidar',
            executable='rtf_urg',
            name='lidar',
            # parameters=[
            #     {'turtlename': 'turtle1'}
            # ]
        ),
        Record(
            name='my_recorder',
            parameters=[{
                'topics': LaunchConfiguration('my_topic_list')
            }]
        ),
    ])
