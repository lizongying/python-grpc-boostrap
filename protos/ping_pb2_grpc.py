# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import ping_pb2 as protos_dot_ping__pb2


class PingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PingCode = channel.unary_unary(
                '/PingService/PingCode',
                request_serializer=protos_dot_ping__pb2.PingCodeRequest.SerializeToString,
                response_deserializer=protos_dot_ping__pb2.PingCodeResponse.FromString,
                )
        self.PingMessage = channel.unary_unary(
                '/PingService/PingMessage',
                request_serializer=protos_dot_ping__pb2.PingMessageRequest.SerializeToString,
                response_deserializer=protos_dot_ping__pb2.PingMessageResponse.FromString,
                )


class PingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PingCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PingMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PingCode': grpc.unary_unary_rpc_method_handler(
                    servicer.PingCode,
                    request_deserializer=protos_dot_ping__pb2.PingCodeRequest.FromString,
                    response_serializer=protos_dot_ping__pb2.PingCodeResponse.SerializeToString,
            ),
            'PingMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.PingMessage,
                    request_deserializer=protos_dot_ping__pb2.PingMessageRequest.FromString,
                    response_serializer=protos_dot_ping__pb2.PingMessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PingCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PingService/PingCode',
            protos_dot_ping__pb2.PingCodeRequest.SerializeToString,
            protos_dot_ping__pb2.PingCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PingMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PingService/PingMessage',
            protos_dot_ping__pb2.PingMessageRequest.SerializeToString,
            protos_dot_ping__pb2.PingMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
