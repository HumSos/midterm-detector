#pip install grpcio
#pip install grpcio-tools
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
    
    def terminate_server(signum, frame):
        print("Got signal {}, {}".format(signum,frame))
        rospy.signal_shutdown("Ending ROS Node")
        terminate.set()

    if __name__ == "__main__":
        print("---ROS GRCP Wrapper--")
        signal.signal(signal.SIGINT, terminate_server)

        print("Starting ROS Node")
        rospy.init_node('object_position_wrapper', anonymous=True)

        print("Starting GRPC server")
        server_addr = "[::]:7042"
        service = RCPDemoImpl()
        server = grcp.server(futures.ThreadPoolExecutor(max_workers=10))
        rpc_demo_pb2_grpc.add_RPCDemoServicer_to_server(service, server)
        server.add_insecure_port(server_addr)
        server.start()
        print("grpc Server listening on" + server_addr)

        print("Running ROS Node")
        rospy.spin()

        terminate.wait()
        print("Stopping GRPC Server")
        server.stop(1).wait(
            print("Exited")
        )

