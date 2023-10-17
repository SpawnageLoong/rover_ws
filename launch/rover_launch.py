from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    start_npm = ExecuteProcess(
        cmd=[['npm run dev --prefix ~/rover_ws/rover-webui']],
        shell=True
    )

    start_motion = ExecuteProcess(
        cmd=[['motion']],
        shell=True
    )

    return LaunchDescription([
        Node(
            package='rover_base',
            executable='rover_base',
            name='rover_base'
        ),
        Node(
            package='rover_serialise',
            executable='rover_serialise',
            name='rover_serialise'
        ),
        Node(
            package='rover_deserialise',
            executable='rover_deserialise',
            name='rover_deserialise'
        ),
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            name='rosbridge_websocket'
        ),
        start_npm,
        start_motion
    ])
