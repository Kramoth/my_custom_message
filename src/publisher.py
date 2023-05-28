#!/usr/bin/env python3
import rospy
from my_custom_message.msg import my_message


def talker():
	rospy.init_node("publisher")
	pub=rospy.Publisher("published_topic",my_message,queue_size=10)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		msg=my_message()
		msg.flag.data="hello"
		msg.is_active.data=True
		msg.value.data=42
		pub.publish(msg)
		rate.sleep()


if __name__=="__main__":
	talker()
