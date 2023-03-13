import grpc
import time
import unary.unary_pb2_grpc as pb2_grpc
import unary.unary_pb2 as pb2

from concurrent import futures

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        result = f'Hello I am up and running received {request.message.key} : {request.message.value}'

        for i in range(2401):
            reply = {
                'message': "Hello",
                'value': i
            }
            yield pb2.MessageResponse(**reply)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()