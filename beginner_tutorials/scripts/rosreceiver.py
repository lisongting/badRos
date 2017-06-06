#!/usr/bin/env python
import rospy
from  beginner_tutorials.msg import TtsStatus

def callback(data):
	rospy.loginfo('get %s %s',data.id,data.idplaying)

def getter():
	rospy.init_node('receiver', anonymous=True)
   	rospy.Subscriber('tts_status', TtsStatus, callback)
	rospy.spin()

if __name__ == '__main__':
	getter()

