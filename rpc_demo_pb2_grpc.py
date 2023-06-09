# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import rpc_demo_pb2 as rpc__demo__pb2


class RPCDemoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getMultCoords = channel.unary_unary(
                '/RPCDemoPkg.RPCDemo/getMultCoords',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=rpc__demo__pb2.MultCoords.FromString,
                )


class RPCDemoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getMultCoords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCDemoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getMultCoords': grpc.unary_unary_rpc_method_handler(
                    servicer.getMultCoords,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=rpc__demo__pb2.MultCoords.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RPCDemoPkg.RPCDemo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPCDemo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getMultCoords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPCDemoPkg.RPCDemo/getMultCoords',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            rpc__demo__pb2.MultCoords.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
