# 17625-a3

## ProtoBuf

1. Book, featuring fields:
    - ISBN - a unique string id (a primary key)
    - title - a string
    - author - a string name, for simplicity (normally a separate PB)
    - genre (an enum field, come up with a list of 3-4)
    - publishing year - an integer
2. InventoryItem:
    - inventory number - kind of, a primary key
    - a `Oneof` field, which can only refer to a Book object. In the future extensions, we might add more supported types.
    - status - an enum of "available", "taken"


Use the following command to compile the proto file to Python stubs (output to service/)

```
    protoc -I protos/ --python_out=service/ protos/book.proto
```

## gRPC

1. CreateBook
   - input: Book
   - output: ISBN, or error (if ISBN already exists)
2. GetBook
   - input: ISBN
   - output: Book Details, or error (if ISBN does not exist)

Use the following command to compile the proto file to Python stubs (output to service/)

```
    python -m grpc_tools.protoc -I protos/ --python_out=service/ --grpc_python_out=service/ protos/inventoryservice.proto
```

## Server

To run the server, use the following command:

```
    python service/server.py
```

The default port is 50051.

**The server gRPC was tested using Postman, and the screenshots is in the `screenshots/a3` folder.**

## Client

To run the client, use the following command:

```
    PYTHONPATH=service python client/get_book_titles.py
```

## Client Tests

To run the tests, use the following command:

```
    PYTHONPATH=service:client python -m unittest client/test.py
```

Note: `test_get_book_titles_live_server` is a live server test, and it will fail if the server is not running.

**The screenshots of client tests is in the `screenshots/a4` folder.**
