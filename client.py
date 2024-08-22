# socket module allows us to create network connections using TCP/IP & other protocols
import socket

'''
This function is responsible for starting the echo client.

Network Basics:
- The client connects to a server running on a specified host and port.
- In this case, we're using '127.0.0.1' (localhost) as the default host, which means the client will connect to a server running on the same machine.
- The default port is 8080, which should match the port the server is listening on.

How it works:
1. Socket Creation: The client creates a TCP socket.
2. Connection: The client attempts to connect to the server using the provided host and port.
3. Communication: Once connected, the client enters a loop where it can send messages to the server and receive responses.
4. Termination: The client can terminate the connection by typing 'quit'.

Important Notes:
- This client uses TCP (SOCK_STREAM) for reliable, connection-oriented communication.
- The client uses blocking I/O, which means operations like connect() and recv() will wait until they complete before the program continues.
- Error handling is implemented to catch and report common issues like connection refusal.
- The client encodes outgoing messages to bytes and decodes incoming messages from bytes, as socket communication occurs in bytes.

Parameters:
- host='127.0.0.1': The IP address of the server to connect to. '127.0.0.1' refers to the localhost (the same machine).
- port=8080: The port number on which the server is listening. This should match the server's port.
'''
def start_client(host='127.0.0.1', port=8080):
    try:
        # CREATE A SOCKET
        # AF_INET specifies that socket will use IPv4 addresses
        # SOCK_STREAM specifies that socket will use TCP
        # socket.socket() creates a new socket object
        # with statement is used to ensure that the socket is closed when done
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # CONNECT TO THE SERVER
                # This initiates a connection to the server at the specified host and port
                s.connect((host, port))
                print(f"Connected to server at {host}:{port}")
                
                # MAIN COMMUNICATION LOOP
                while True:
                    # Prompt the user for input
                    message = input("Enter message (or 'quit' to exit): ")
                    
                    # Check if the user wants to quit
                    if message.lower() == 'quit':
                        break
                    
                    # SEND THE MESSAGE
                    # encode() converts the string to bytes, which is required for socket communication
                    s.sendall(message.encode())
                    
                    # RECEIVE THE RESPONSE
                    # recv(1024) reads up to 1024 bytes from the socket
                    # This is a blocking call - it will wait until data is received
                    data = s.recv(1024)
                    
                    # Print the received data, decoding it back to a string
                    print(f"Received: {data.decode()}")
            
            except ConnectionRefusedError:
                # This error occurs if the server is not running or not accepting connections
                print(f"Connection to {host}:{port} was refused. Is the server running?")
    
    except Exception as e:
        # Catch any other exceptions that might occur
        print(f"An error occurred: {e}")

# This is the main entry point of the client.
# It runs the client when this script is executed directly (i.e., python client.py)
if __name__ == "__main__":
    start_client()