# socket module allows us to create network connections using TCP/IP & other protocols
import socket

'''
This function is responsible for starting the echo server.

Network Basics:
- "host" is the IP address the server binds to. In this case, '127.0.0.1' is used, which is always associated with the loopback interface.
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
- The server handles connections sequentially, which is typical for a basic implementation. This approach may be a limitation for high-traffic scenarios. More advanced servers might use threading or asynchronous I/O to handle multiple connections simultaneously.

Parameters:
- host='127.0.0.1': The IP address to listen on. '127.0.0.1' means "listen only for local connections".
- port=8080: The port number to listen on. On Unix-like systems (Linux, macOS), ports below 1024 typically require admin privileges. This restriction may not be as strict on Windows systems.
'''
def start_server(host='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server is running on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

if __name__ == '__main__':
    start_server()