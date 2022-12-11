import logging

import grpc
import inventoryservice_pb2
import inventoryservice_pb2_grpc


class InventoryClient:
    def __init__(self, addr="localhost", port=50051):
        self.channel = grpc.insecure_channel(f"{addr}:{port}")
        self.stub = inventoryservice_pb2_grpc.InventoryServiceStub(self.channel)

    def create_book(self, book):
        """Client call to create a book."""
        try:
            response = self.stub.CreateBook(book)
        except grpc.RpcError as e:
            logging.info(f"CreateBook failed with {e.code()}: {e.details()}")
            return None
        logging.info(f"Created book with ISBN {response.ISBN}")
        return response.ISBN

    def get_book(self, ISBN):
        """Client call to get a book by ISBN."""
        try:
            response = self.stub.GetBook(inventoryservice_pb2.GetBookRequest(ISBN=ISBN))
        except grpc.RpcError as e:
            logging.info(f"GetBook failed with {e.code()}: {e.details()}")
            return None
        logging.info(f"Got book with ISBN {response.book.ISBN}")
        return response.book
