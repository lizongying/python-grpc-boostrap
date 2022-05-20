from protos import ping_pb2
from protos import ping_pb2_grpc


class PingService(ping_pb2_grpc.PingService):
    def PingCode(self, request, context, *args, **kwargs):
        return ping_pb2.PingCodeResponse(
            request_id=request.request_id,
            data=ping_pb2.PingCodeData(
                code=200,
            ),
        )

    def PingMessage(self, request, context, *args, **kwargs):
        return ping_pb2.PingMessageResponse(
            request_id=request.request_id,
            data=ping_pb2.PingMessageData(
                message='ok',
            ),
        )
