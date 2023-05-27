#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class cameraNode:
    def __init__(self):
        rospy.init_node('camera_node', anonymous=True)
        self.pub = rospy.Publisher('/camera/rgb/image_raw', Image, queue_size=10)
        self.update(self)

    def update(self):
        frame = cv2.imread("green_ball.jpg")
        self.pub.Publish(frame)

if __name__ == '__main__':
    cam = cameraNode()
    try:
        cam.update()
        rospy.spin()
    except KeyboardInterrupt:
        print("Apagando camera node...")
