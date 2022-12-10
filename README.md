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
