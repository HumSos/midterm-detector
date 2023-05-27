#!/usr/bin/env python3
import time
from concurrent import futures

import grpc
import rospy
from geometry_msgs.msg import PointStamped

import PositionService_pb2
import PositionService_pb2_grpc

class PositionServiceServicer(PositionService_pb2_grpc.PositionServiceServicer):
    def __init__(self):
        self.latest_message = PointStamped()
        rospy.init_node('position_listener', anonymous=True)
        rospy.Subscriber("/camera/marker_center", PointStamped, self.callback)
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


    def callback(self, data):
        self.latest_message = data

    def SendPosition(self, empty, context):
        if self.latest_message is not None:
            response = PositionService_pb2.Position()
            response.x = self.latest_message.point.x
            response.y = self.latest_message.point.y
            response.timestamp = self.latest_message.header.stamp.nsecs
            return response
        else:
            raise grpc.RpcError("No position data received yet")

    def serve(self):
        PositionService_pb2_grpc.add_PositionServiceServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()

    def serverStop(self):
        self.server.stop(0)
    


if __name__ == '__main__':
    servicer = PositionServiceServicer()
    servicer.serve()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        servicer.serverStop()
