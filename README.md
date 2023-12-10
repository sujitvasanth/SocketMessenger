# SocketMessenger
simple socket messager (proof of concept)

This is a simple proof of concept written with chat GPT.
you should put client.py, server.py and socketstart.py all in the same folder.
Run socketstart.py which should initiate the server and client and do any open/close of sockets

The killswitch for the server is the connection of a second client, this in turn sends a kill switch the the client neatly closing all the messaging instances making it platform agnostic.

![Screenshot from 2023-12-10 14-47-01](https://github.com/sujitvasanth/SocketMessenger/assets/18464444/ea1a5c87-567d-4047-b8fb-b8c407fcf19e)
