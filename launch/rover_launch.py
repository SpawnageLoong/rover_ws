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
            namespace='rover',
            executable='rover_base',
            name='rover_base'
        ),
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            name='rosbridge_websocket'
        ),
        start_npm,
        start_motion
    ])
