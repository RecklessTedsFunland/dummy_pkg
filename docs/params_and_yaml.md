# params and yaml

## Format

```yaml
node_namespace: # optional
    node_name:
        ros__parameters:
            param: value
            param: value
            ...
            param_namespace:
                param: value
                ...
    node_name_2:
        ros__parameters:
            param: value
            ...
```

## CLI

```bash
ros2 run <package> <node> --ros-args --params-file <filename>.yaml
ros2 param list
ros2 param set <node> <parameter> <value>
ros2 param dump <node>
ros2 param dump <node> > file.yaml
```

## Launch File

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # read package yaml
    config = os.path.join(
        get_package_share_directory('ros2_tutorials'),
        'config',
        'params.yaml'
        )

    return LaunchDescription([
        Node(
            package=<package>,
            executable=<node>,
            output="screen",  # output printed to console
            emulate_tty=True, # output printed to console
            parameters=[
                {"param": value}
                ...
            ]
        ),
        Node(
            package = <package>,
            executable = <node>,
            name = 'your_amazing_node',
            parameters = [config]
        )
    ])
```

## C++ Callback

```c++
std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle_;
this->declare_parameter("an_int_param", 0);
// Set a callback for this node's integer parameter, "an_int_param"
auto cb = [this](const rclcpp::Parameter & p) {
    RCLCPP_INFO(
        this->get_logger(), "cb: Received an update to parameter \"%s\" of type %s: \"%ld\"",
        p.get_name().c_str(),
        p.get_type_name().c_str(),
        p.as_int());
    };
cb_handle_ = param_subscriber_->add_parameter_callback("an_int_param", cb);
```

[ros2 tutorial](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Monitoring-For-Parameter-Changes-CPP.html)

## Python Callback

```python
self.declare_parameter('an_int_param', 0)
self.handler = ParameterEventHandler(self)
self.callback_handle = self.handler.add_parameter_callback(
    parameter_name="an_int_param",
    node_name="node_with_parameters",
    callback=self.callback,
)

def callback(self, p: rclpy.parameter.Parameter) -> None:
    self.get_logger().info(f"Received an update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}")
```

[ros2 tutorial](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Monitoring-For-Parameter-Changes-Python.html)

## Python Pass YAML to Node

In python source code:

```python
import rclpy
from rclpy.node import Node

class TestYAMLParams(Node):

    def __init__(self):
        super().__init__('your_amazing_node')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bool_value', None),
                ('int_number', None),
                ('float_number', None),
                ('str_text', None),
                ('bool_array', None),
                ('int_array', None),
                ('float_array', None),
                ('str_array', None),
                ('bytes_array', None),
                ('nested_param.another_int', None)
            ])

def main(args=None):
    rclpy.init(args=args)
    node = TestYAMLParams()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

[roboticsbackend.com params](https://roboticsbackend.com/ros2-yaml-params/)

Launch file:

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('ros2_tutorials'),
        'config',
        'params.yaml'
        )

    node=Node(
        package = 'ros2_tutorials',
        name = 'your_amazing_node',
        executable = 'test_yaml_params',
        parameters = [config]
    )

    ld.add_action(node)
    return ld
```