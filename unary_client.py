import grpc
import json
import unary.unary_pb2_grpc as pb2_grpc
import unary.unary_pb2 as pb2

import time
import numpy as np


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """

        message = pb2.Message(message=message)

        values = []
        replies = self.stub.GetServerResponse(message)
        for reply in replies:
            values.append(reply.value)

        return values

if __name__ == '__main__':
    client = UnaryClient()
    point = pb2.Point(key="A", value=2)
    start = time.time()
    data = client.get_url(message=point)

    print(time.time() - start)