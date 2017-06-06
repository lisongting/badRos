#!/usr/bin/env python
import rospy
from  beginner_tutorials.msg import Num

def callback(data):
	rospy.loginfo('get %s %s',data.num,data.doing)

def getter():
	rospy.init_node('getter', anonymous=True)
   	rospy.Subscriber('museum_position', Num, callback)
	rospy.spin()

if __name__ == '__main__':
	getter()

