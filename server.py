# socket module allows us to create network connections using TCP/IP & other protocols
import socket

'''
This function is responsible for starting the echo server.

Network Basics:
- "host" is the IP address the server binds to. In this case, '127.0.0.1' (also known as "localhost") is used, which is always associated with the loopback interface.
- The loopback interface is a special network interface that allows a device to communicate with itself.
- The '127.0.0.0/8' range is reserved for loopback addresses.

How it works:
1. Binding: The server "binds" its socket to the specified IP address and port.
2. OS Role: The operating system (OS) manages the relationship between IP addresses and network interfaces:
   - It maintains a mapping of IP addresses to network interfaces.
   - When you bind to '127.0.0.1', the OS knows to use the loopback interface.
3. Listening: Once bound, the server listens for incoming connections on the specified interface and port.
4. Connection Handling: Any incoming connections to '127.0.0.1' on the specified port are routed to this server.

Important Notes:
- While an IP address is not the same as a network interface, they are closely linked.
- The port number (8080 in this case) allows multiple services to use the same IP address, differentiated by port.
- This server uses TCP (SOCK_STREAM) for reliable, connection-oriented communication.
- The server uses blocking I/O and handles connections sequentially, which is typical for a basic implementation. This approach may be a limitation for high-traffic scenarios. More advanced servers might use threading or asynchronous I/O to handle multiple connections simultaneously.
- If you want to accept connections from other machines on the network, you'd typically use '0.0.0.0' or a specific network interface IP (rather than '127.0.0.1').

Parameters:
- host='127.0.0.1': The IP address to listen on. '127.0.0.1' means the server will only accept connections from the same machine (i.e., the very same machine that the server is running on).
- port=8080: The port number to listen on. On Unix-like systems (Linux, macOS), ports below 1024 are considered "privileged" and typically require admin privileges. This restriction may not be as strict on Windows systems.
'''
def start_server(host='127.0.0.1', port=8080):
    # CREATE A SOCKET
    # AF_INET specifies that socket will use IPv4 addresses
    # SOCK_STREAM specifies that socket will use TCP (i.e. the protocol for connection-oriented communication)
    # socket.socket() creates a new socket object
    # with statement is used to ensure that the socket is closed when done
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # BIND THE SOCKET TO THE HOST AND PORT
        # This associates the socket with the specified IP address and port, preparing it for listening.
        # Behind the scenes, the OS maps the IP address to the appropriate network interface.
        s.bind((host, port))
        # LISTEN FOR INCOMING CONNECTIONS (listening mode activated)
        # This allows the server to accept incoming connections.
        s.listen()
        print(f"Server is running on {host}:{port}")
        # Starts an infinite loop that waits for incoming connections.
        while True:
            # Accepts an incoming connection.
            # accept() blocks (waits) until a client connects to the server. When a client connects, it returns a new socket object (conn) representing the connection and a tuple (addr) containing the client's address.
            conn, addr = s.accept()
            # with statement is used to ensure that the connection (conn) is properly closed when the block is exited.
            with conn:
                print(f"Connected by {addr}")
                # Starts a loop that handles incoming data. Keeps connection with client open until client closes connection.
                while True:
                    # Reads data from the client.
                    # conn.recv(1024) is a blocking call that waits for data to arrive from the client. It returns the data as a bytes object. recv() reads data from the socket into a buffer (1024 bytes in this case).
                    data = conn.recv(1024)
                    # If no data is available to be read, it typically means the client has closed the connection.
                    if not data:
                        # Exit the loop, which will close the connection when the 'with' block ends.
                        break
                    # Sends all the read data back to the client.
                    # This is the "echo" part of the echo server, where the server sends back exactly what it reads from the client.
                    conn.sendall(data)

# This is the main entry point of the server.
# Starts the server when this script is run directly (i.e., python server.py), rather than imported as a module.
if __name__ == '__main__':
    # Starts the server.
    start_server()