import json
from uuid import uuid4

import grpc
from google.protobuf.json_format import MessageToJson

from protos import ping_pb2
from protos import ping_pb2_grpc
from settings import *


def run():
    """
    三个测试服务
    :return:
    """
    channel = grpc.insecure_channel(HOST)
    stub = ping_pb2_grpc.PingServiceStub(channel)
    response = stub.PingCode(ping_pb2.PingCodeRequest(
        request_id=str(uuid4()),
    ))
    print(json.dumps(json.loads(MessageToJson(response)), indent=2, ensure_ascii=False))

    response = stub.PingMessage(ping_pb2.PingMessageRequest(
        request_id=str(uuid4()),
    ))
    print(json.dumps(json.loads(MessageToJson(response)), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    run()
