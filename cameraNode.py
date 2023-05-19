#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2

class cameraNode:
    def __init__(self):
        rospy.init_node('camera_node', anonymous=True)
        self.pub = rospy.Publisher('/camera/rgb/image_raw', Image, queue_size=10)
        self.update(self)

    def update(self):
        cp = cv2.VideoCapture(0)
        if not cp.isOpened():
            print("Cannot open the camera")
        ret, frame = cp.read()
        self.pub.Publish(frame)

if __name__ == '__main__':
    cam = cameraNode()
    cam.update()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Apagando camera node...")
