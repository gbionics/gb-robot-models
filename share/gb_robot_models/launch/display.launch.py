from pathlib import Path

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    package_share = Path(__file__).resolve().parent.parent
    urdf_path = package_share / "robots" / "gene01_0" / "model.urdf"
    rviz_config_path = package_share / "rviz" / "display.rviz"
    robot_description = urdf_path.read_text(encoding="utf-8")

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": robot_description}],
            output="screen",
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            output="screen",
        ),
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["0", "0", "1.0", "0", "0", "0", "map", "pelvis"],
            output="screen",
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", str(rviz_config_path)],
            output="screen",
        ),
    ])
