import signal
import threading
from concurrent import futures
from std_msgs.msg import Float64MultiArray
import rospy

import sys
import grpc
sys.path.insert(1,'./protos')
import rpc_demo_pb2
import rpc_demo_pb2_grpc



class RPCDemo(rpc_demo_pb2_grpc,RPCDemoServicer):
    def __init__(self):
        self.data = [0,0,0]
        rospy.subscriber('/object_position', Float64MultiArray, self.updateData)
        print("initialized grpc server")

    def updateData(self, data):
        self.data[0] = data.data[0]
        self.data[1] = data.data[1]
        self.data[2] = data.data[2]

    def getMultCoords(self, request, context):
        print("Got call: "+ context.peer())
        results = rpc_demo_pb2.MultCoords()
        results.values.append(self.data[0])
        results.values.append(self.data[1])
        results.values.append(self.data[2])
        return results

