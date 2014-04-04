cmake_minimum_required(VERSION 2.8.3)
project(rxbag_plugins)
find_package(catkin REQUIRED)


# This was taken from rqt_bag_plugins as example

find_package(rxbag REQUIRED COMPONENTS
std_msgs
geometry_msgs
sensor_msgs
roslib
rospy
)

catkin_python_setup()

catkin_package()

install(FILES plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
