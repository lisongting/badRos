#!/usr/bin/env python
import rospy
from  beginner_tutorials.msg import Num

def sender():
	pub = rospy.Publisher('museum_position',Num,queue_size=10)
	rospy.init_node('myRos',anonymous=True)
	rate = rospy.Rate(5)
	a = 1
	while not rospy.is_shutdown():
		number = Num()
		number.num = a
		if a%2==0:
			number.m = 55
		else:
			number.m = 66
		print('sending:',number.num,number.m)		
		a=a+1
		pub.publish(number)
		rate.sleep()
			

if __name__ == '__main__':
	try:
	    sender()
	except rospy.ROSInterruptException:
            pass


