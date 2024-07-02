from launch import LaunchDescription
from launch_ros.actions import Node
# from rosbag2.launch_actions import Record

# Ref
# https://github.com/foxglove/ros-foxglove-bridge

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="foxglove_bridge",
            executable="foxglove_bridge",
            name="foxglove_bridge",
            parameters=[
                {"port": 8765},
                {"address": "0.0.0.0"},
                {"tls": False},
                {"topic_whitelist": [".*"]},
                {"send_buffer_limit": 10000000},
                {"use_sim_time": False},
                {"num_threads": 0}
            ]
        ),
        Node(
            package="rtf_pyopencv_camera",
            executable="pycamera",
            name="camera"
        )
        # Node(
        #     package='rtf_sensors',
        #     executable='rtf_imu',
        #     name='imu'
        # ),
        # Node(
        #     package = "tf2_ros",
        #     executable = "static_transform_publisher",
        #     arguments = ["0","0","0","0","0","0","world","laser"]
        # ),
        # Node(
        #     package='rtf_lidar',
        #     executable='rtf_urg',
        #     name='lidar',
        #     # parameters=[
        #     #     {'turtlename': 'turtle1'}
        #     # ]
        # ),
        # Record(
        #     name='my_recorder',
        #     parameters=[{
        #         'topics': LaunchConfiguration('my_topic_list')
        #     }]
        # ),
    ])
