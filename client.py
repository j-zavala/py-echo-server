import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received: {data.decode()}")

if __name__ == "__main__":
    start_client()