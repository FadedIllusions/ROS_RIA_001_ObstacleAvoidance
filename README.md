# ROS_RIA_001_ObstacleAvoidance

Brief Notes Taken Over Proceeding Sections:

```
Note: Services vs Actions. When you call a service, the robot has to wait until service has ended before doing anything else. When you call an action, your robot can still keep doing something else while performing the action.


ROS Launch Node Parameters Explained
------------------------------------
    <node pkg="package_name" type="python_file_name.py" name="node_name" output="type_of_output" />

  *  pkg="package_name"
     Name of package that contains code of ROS program to execture
  *  type="python_file_name.py"
     Name of program file to execute
  *  name="node_name"
     ROS node that will launch our python file
  *  output="type_of_output"
     Channel to which to print the output of python file


Launch ROS Package
roslaunch <package_name> <launch_file>
--------------------------------------
* roslaunch turtlebot_teleop keyboard_teleop.launch


Use roscd To CD Into Package
----------------------------
* roscd turtlebot_teleop


Create ROS Package
catkin_create_pkg <package_name> <package_dependencies>
-------------------------------------------------------
* cd into catkin_ws/src
* catkin_create_pkg my_package rospy


Check If Package Created
rospack list | grep <package_name>
----------------------------------
* rospack list | grep my_package
* roscd my_package


List ROS Nodes
--------------
* rosnode list


Display Node Info
rosnode info /<node_name>
-----------------
* rosnode info /ObiWan


Compile Package
(Compiles entire catkin_ws directory)
-------------------------------------
* catkin_make

Note: Sometimes (for example, in large projects) you will not want to compile all of your packages, but just the one(s) where you've made changes. Use: 'catkin_make --only-pkg-with-deps <package_name>'


List Parameters
---------------
* rosparam list
* To Get Value Of Parameter:
  rosparam get <parameter_name>
* To Set Value Of Parameter:
  rosparam set <parameter_name> <value>

Ex: To get the value of '/camera/imager_rate' and change it to 4.0:
* rosparam get /camera/imager_rate
* rosparam set /camera/imager_rate 4.0


Confirm Topic Running
---------------------
* rostopic list | grep '/counter'
* rostopic info /counter


RealTime Check Of Topic Info
----------------------------
* rostopic echo /counter


Get List Of Available Topics
----------------------------
* rostopic list


Note: Display information being published by a topic...'rostopic echo <topic_name>'. To read only the last message published... 'rostopic echo <topic_name> -n1'.

To get information on the Int32 message, use 'rosmsg show std_msgs/Int32'. In this case, Int32 has only one variable named 'data' of type 'int32'.
```
