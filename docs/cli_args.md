# CLI Args

```bash
ros2 run <package_name> <executable_name> --ros-args -p <param_name>:=<value>
ros2 run my_package my_node --ros-args -p message:="Hello, ROS 2!"
```

```bash
ros2 run <package_name> <executable_name> --ros-args -r <remap>
```

- remap namespace:
    - `__ns:=/new/namespace`
    - `node1:__ns:=/node1s/new/namespace`
- remap name/node (these are the same)
    - `__name:=left_camera_driver`
    - `__node:=left_camera_driver`
    - `camera_driver:__name:=left_camera_driver`

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    my_arg = DeclareLaunchArgument('my_arg', default_value='default_value')

    return LaunchDescription([
        my_arg,
        # other launch actions using 'my_arg'
    ])
```

[ros2 how-to node args](https://docs.ros.org/en/jazzy/How-To-Guides/Node-arguments.html)