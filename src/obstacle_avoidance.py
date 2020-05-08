#! /usr/bin/env python

# Import Needed Packages
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



# Define LaserScan Subscriber Callback
def callback(msg):
    # Print Distance To Obstacle In Front Of Robot
    # print msg.ranges[360]

    # If Distance > 1 Meter, Move Robot Forward
    if msg.ranges[360] > 1:
        move.linear.x = 0.1
        move.angular.z = 0.0

    # If Distance < 1 Meter, Turn Robot Right
    if msg.ranges[360] < 1:
        move.linear.x = 0.0
        move.angular.z = -0.2

    # If Obstacle On Right Of Robot && Distance Of Obstacle < 0.5 Meters,
    # Turn Robot Left
    if msgs.ranges[0] < 0.5:
        move.linear.x = 0.0
        move.angular.z = 0.2

    # If Obstacle On Left Of Robot && Distance Of Obstacle < 0.5 Meters,
    # Turn Robot Right
    if msgs. ranges[719] < 0.5:
        move.linear.x = 0.0
        move.linear.z = -0.2

    # Publish Twist Msg To /cmd_vel
    pub.publish(move)


# Init Rospy Node 
rospy.init_note('obstacle_avoidance_node')

# Instantiate LaserScan Subscriber Object -- Subscribe To Laser Topic
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

# Instantiate Cmd Vel Publisher
pub = rospy.Publisher('/cmd_vel', Twist)

move = Twist()

rospy.spin()
