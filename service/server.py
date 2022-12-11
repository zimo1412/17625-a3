"""The python service for bookstore."""

from concurrent import futures
import logging

import grpc
from grpc_reflection.v1alpha import reflection
import inventoryservice_pb2
import inventoryservice_pb2_grpc

from database import BookStore


class InventoryService(inventoryservice_pb2_grpc.InventoryServiceServicer):
    def CreateBook(self, request, context):
        db = BookStore()
        success, ISBN, message = db.create_book(request.book)
        logging.info(f"CreateBook: {success}, {ISBN}, {message}")
        if not success:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(message)
        return inventoryservice_pb2.CreateBookResponse(ISBN=ISBN)

    def GetBook(self, request, context):
        db = BookStore()
        success, book, message = db.get_book(request.ISBN)
        logging.info(f"GetBook: {success}, {book}, {message}")
        if not success:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(message)
        return inventoryservice_pb2.GetBookResponse(book=book)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventoryservice_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    
    # Reflection of service
    SERVICE_NAMES = (
        inventoryservice_pb2.DESCRIPTOR.services_by_name['InventoryService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    
    
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server started on port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
