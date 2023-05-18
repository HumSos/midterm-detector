#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import ctypes
from time import time 
import numpy as np
from std_msgs.msg import Float64MultiArray

so="../CPP-LIN-Linux/src/cpp_lib_demo.so"

class GreenDetector:
    def __init__(self):
        rospy.init_node('green_detector', anonymous=True)
        pub=rospy.Publisher('/green_detector',Float64MultiArray,queue_size=10)
        rate=rospy.rate(100)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        
    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            cv_image = cv2.resize(cv_image,(640,480))
        except CvBridgeError as e:
            print(e)
        
        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        lower_green = (40, 50, 50) # Establece el rango de valores de HSV para el color verde
        upper_green = (80, 255, 255)
        mask = cv2.inRange(hsv, lower_green, upper_green) # Crea una máscara con los pixeles verdes

        kernel = np.onex((5,5),np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Encuentra el contorno más grande (el objeto verde más grande en la imagen)
            c = max(contours, key=cv2.contourArea)
            # Encuentra el centroide del contorno
            M = cv2.moments(c)
            x,y,w,h=cv2.boundingRect(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("Coordenadas del objeto verde: ({}, {})".format(cx, cy))
            cv2.rectangle(hsv,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imgshow('img',hsv)
        cv2.waitKey(1)

if __name__ == '__main__':

    mylib = ctypes.CDLL(so)
    in_val=([0.0,0.0])
    out_val=([0.0,0.0])
    gd = GreenDetector()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Apagando green_detector")
    cv2.destroyAllWindows()
