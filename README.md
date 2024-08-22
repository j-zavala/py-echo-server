# Echo Server

A simple echo server that can be used to test client-server communication via TCP/IP.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Diagrams](#diagrams)
- [Video Walkthrough](#video-walkthrough)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Echo Server is a simple yet powerful tool designed for testing and demonstrating basic client-server communication using TCP/IP protocols. This project aims to provide developers, network administrators, and students with a straightforward implementation of a server that echoes back any message it receives from a client.

Key features and functionalities include:

1. TCP/IP Communication: Utilizes standard socket programming to establish reliable connections between clients and the server.

2. Concurrent Client Handling: Capable of managing multiple client connections simultaneously, allowing for scalability testing.

3. Cross-Platform Compatibility: Developed in Python, ensuring compatibility across various operating systems.

4. Minimal Dependencies: Relies solely on Python's built-in libraries, making it easy to set up and run without additional installations.

5. Customizable Port: Allows users to specify the port number, facilitating testing on different network configurations.

6. Logging: Implements basic logging to track incoming connections and messages for debugging and monitoring purposes.

7. Graceful Shutdown: Includes mechanisms for properly closing connections and shutting down the server.

This Echo Server serves as an excellent starting point for learning about network programming, debugging network issues, and testing client applications. It can be particularly useful in scenarios such as:

- Verifying network connectivity between systems
- Testing firewall configurations
- Demonstrating basic client-server architecture in educational settings
- Serving as a foundation for more complex server implementations

By providing a simple yet functional echo service, this project helps solve common problems in network testing and education, offering a hands-on approach to understanding the fundamentals of client-server communication.

### Technologies Used

- Language: Python 3.9.6
- Key Libraries/Tools:
  - socket: Built-in Python module for network programming
  - No external dependencies required

The project utilizes Python's standard library, specifically the `socket` module, to implement the Echo Server and Client. This approach ensures minimal setup requirements and cross-platform compatibility.

Key components:
1. Server implementation:
```python:server.py
startLine: 31
endLine: 65
```
2. Client implementation:
```python:client.py
startLine: 28
endLine: 61
```

By leveraging Python's built-in capabilities, the project maintains simplicity while demonstrating fundamental concepts of network programming.

## Installation

### Prerequisites
- Python 3.9.6 or higher

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/jzavala/echo-server.git
   ```

2. Navigate to the project directory:
   ```bash
   cd echo-server
   ```

3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv echo-server-venv
   source echo-server-venv/bin/activate  # On Windows, use `echo-server-venv\Scripts\activate`
   ```

4. Install dependencies:
   As this project uses only Python's standard library, there are no external dependencies to install. However, if you add dependencies in the future, you can install them using:
   ```bash
   pip install -r requirements.txt
   ```

The project is now set up and ready to run. No additional configuration is required.

Note: The `.gitignore` file is already set up to exclude common Python and environment-specific files:

```python:.gitignore
startLine: 1
endLine: 45
```

This ensures that only necessary project files are tracked by version control.

## Usage

### Running the Server
To start the Echo Server, run the following command in your terminal:

```bash
python server.py
```

You can also specify a custom port number by providing it as an argument:

```bash
python server.py 4444
```

This will start the server listening on port 4444.

### Running the Client
To run the client, use the following command:

```bash
python client.py
```

You can also specify the server address and port as arguments:

```bash
python client.py 127.0.0.1 4444
```

This will connect to the server at address 127.0.0.1 and port 4444.

## Examples

### Example 1: Running the Server and Client Locally
```bash
# Start the server
python server.py

# Start the client
python client.py
```

### Example 2: Running the Server and Client on Different Machines
```bash
# Start the server on machine A
python server.py 4444

# Start the client on machine B
python client.py machine_A_ip_address 4444
```

## Diagrams

### TCP Handshake and Data Exchange in an Echo Server

In this section, we provide a visual representation of how the TCP handshake and subsequent data exchange occur between a client and a server in an echo server implementation.

%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
sequenceDiagram
    participant Client
    participant Server

    rect rgb(240,248,255)
    Note over Client,Server: Both Client and Server have their own TCP stack
    Note over Server: s.bind((host, port))
    Note over Server: s.listen()
    Note over Server: Server is ready to accept connections
    end
    
    rect rgb(255,228,225)
    Note over Client: s.connect((host, port))
    Client->>Server: SYN
    Note over Server: s.accept() (blocking, waiting for connection)
    Server-->>Client: SYN-ACK
    Client->>Server: ACK
    Note over Server: s.accept() returns (conn, addr)
    end
    
    rect rgb(144,238,144)
    Note over Client,Server: Connection established
    Client->>Server: s.sendall(message.encode())
    Note over Server: data = conn.recv(1024)
    Server->>Client: conn.sendall(data)
    Note over Client: s.recv(1024)
    Note over Client,Server: Data exchange continues...
    end

    rect rgb(255,248,220)
    Note over Client: Client initiates close
    Client->>Server: FIN
    Server->>Client: ACK
    Server->>Client: FIN
    Client->>Server: ACK
    Note over Client,Server: Connection closed
    end

The diagram illustrates TCP communication from an application-level perspective, specifically focusing on how Python code using sockets interacts with the operating system to manage network communication. If we were to reference the TCP/IP model (or OSI model), this diagram primarily showcases the Application Layer (Layer 7 in the OSI model) and how it interfaces with the underlying layers.

- **Application Layer (Layer 7)**: Your code resides here, making use of network services to perform tasks like sending and receiving messages.
- **Transport Layer (Layer 4)**: Although not explicitly separated, the diagram touches on this layer through the TCP stack's role in ensuring reliable data transmission between the client and server.
- **Operating System Role**: The OS bridges the gap between your application and the network, managing the complexities of TCP communication while providing your code with a straightforward interface (the socket API).

> NOTE: The diagram does not delve into the specifics of the lower layers (such as the Network Layer or Data Link Layer). Instead, it focuses on the higher-level interaction where the application code interfaces with the OS's networking capabilities. The lower layers (which handle routing, addressing, and physical transmission of data) are abstracted away, allowing you to concentrate on the application-level logic.


## Video Walkthrough

[Insert link to video walkthrough or tutorial]

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

[Insert license information]