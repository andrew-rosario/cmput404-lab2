### Lab 2
##### Question 1
In the socket package, you initialize a socket object. By default, it creates a TCP socket, denoted by ```socket.SOCK_STREAM```. in the first argument it accepts.
##### Question 2
Actually, there is no difference. Both server and client sockets are fundamentally the same. For example, the server socket can connect to a host, and also accept connections.

Don't read the below. 

However, there are some differences.
- The server socket accepts connections from client sockets, while the client socket connects to a server socket.
- Server sockets listen for incoming connections from a designated address and port.
- Client sockets connect to a server socket provided they know the address and port to go to.

##### Question 3
Go into your socket options, and change the ```socket.SO_REUSEADDR``` flag to 1. This will allow the socket to reuse the same local address and port. 
##### Question 4
What the client's address is and what port they used to connect to the server.
##### Question 5
The HTTP response message, which is to be expected because we sent a HTTP GET request.

##### Question 6
You're already here.