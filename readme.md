# Dummy Test Package

This is for testing ... not sure what value it is to others. I am just trying out
some ros2 things.

## Nodes

```bash
colcon build --packages-select dummy_pkg
ros2 run dummy_pkg <node>
```

- `dummy_node`: doesn't do anything
- `lidar_node`: publishes a `LaserScan` message
- `transform_node`: publishes a `TransformedStamped` message

## Launch

```bash
ros2 launch dummy_pkg <script>
```

- `tf_launch`
- `rosbag_launch`: run `imu_node` and `urg_node` and stores messages in a bag


### Foxglove

```python
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
)
```

## ROS2 Useful Packages

> **WARNING:** There are already AprilTag `apt` packages available
> and I don't know what the difference is:
> - `sudo apt install ros-jazzy-apriltag` UMich
> - `sudo apt install ros-jazzy-apriltag-ros` Christian Rauch
> - `sudo apt install ros-jazzy-apriltag-detector` Bernd Pfrommer

- [`image_transport` tutorials](https://github.com/ros-perception/image_transport_tutorials/tree/main) for ROS2
- [ROS2 Apriltag detector](https://github.com/christianrauch/apriltag_ros/tree/master): Find apriltags in image
  - subscribe:
    - `image_rect`(`raw`): `sensor_msgs/msg/Image`
    - `image_rect/compressed`: `sensor_msg/msg/CompressedImage`
    - `camera_info`: `sensor_msgs/msg/CameraInfo`
  - publish:
    - `tf`: `tf2_msgs/msg/TFMessage` and `child_frame_id` is set to `tag<family>:<id>` (e.g., `tag36h11:21`)
    - `detections`: `apriltag_msgs/msg/AprilTagDetectionArray`
- [ROS2 Apriltag Messages](https://github.com/christianrauch/apriltag_msgs/tree/master): Broadcast messages of tags
  - `AprilTagDetection`: single tag detection
  - `AprilTagDetectionArray`: multiple tag detections
  - `Point`: 2D x,y point used in above messages
- [Apriltag Draw Marker on Image](https://github.com/christianrauch/apriltag_viz/tree/master): Debug, show Apriltag found in image
  - publish: `tag_detections_image`
  - subscribe:
    - `image`: `image_transport`
    - `detections`: `AprilTagDetectionArray`
  - parameters:
    - `overlay_mode`: `string`, draw axes on image, default is `axes`
    - `image_transport`: default is `raw`
- [libcamera simple camera code](https://github.com/christianrauch/simple-cam/tree/master): maybe useful for writing C++ libcamera driver?

## Other

```bash
$ apt search apriltag
...
apriltag/noble 3.3.0-2.1build1 arm64
  AprilTags Visual Fiducial System

libapriltag-dev/noble 3.3.0-2.1build1 arm64
  AprilTags Visual Fiducial System

python3-apriltag/noble 3.3.0-2.1build1 arm64
  AprilTags Visual Fiducial System
```

## Christian Rauch

```bash
$ sudo apt info ros-jazzy-apriltag-ros
Package: ros-jazzy-apriltag-ros
Version: 3.2.2-1noble.20240607.222731
Priority: optional
Section: misc
Maintainer: Christian Rauch <Rauch.Christian@gmx.de>
Installed-Size: 455 kB
Depends: libc6 (>= 2.34), libconsole-bridge1.0 (>= 1.0.1+dfsg2), libgcc-s1 (>= 3.3.1), libopencv-calib3d406t64 (>= 4.6.0+dfsg), libopencv-core406t64 (>= 4.6.0+dfsg), libstdc++6 (>= 13.1), ros-jazzy-apriltag, ros-jazzy-apriltag-msgs, ros-jazzy-cv-bridge, ros-jazzy-image-transport, ros-jazzy-rclcpp, ros-jazzy-rclcpp-components, ros-jazzy-sensor-msgs, ros-jazzy-tf2-ros, ros-jazzy-ros-workspace
Download-Size: 117 kB
APT-Sources: http://packages.ros.org/ros2/ubuntu noble/main arm64 Packages
Description: AprilTag detection node
```

# MIT License

**Copyright (c) 2024 Reckless Ted's Funland**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
