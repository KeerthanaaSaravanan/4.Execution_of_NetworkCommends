import socket
from pythonping import ping

# Initialize the socket
s = socket.socket()
s.bind(('localhost', 8000))  # Missing comma was causing syntax error
s.listen(5)
print("Server is listening...")

# Accept a client connection
c, addr = s.accept()
print(f"Connected to {addr}")

while True:
    try:
        # Receive the hostname from the client
        hostname = c.recv(1024).decode()

        if not hostname:
            break  # Break if no hostname is received (client disconnected)

        # Attempt to ping the received hostname
        response = ping(hostname, verbose=False)
        c.send(str(response).encode())
    except KeyError:
        # Send "Not Found" if the hostname is invalid or an error occurs
        c.send("Not Found".encode())
    except Exception as e:
        # Catch any unexpected errors
        print(f"Error: {e}")
        c.send(f"Error: {str(e)}".encode())

# Close the socket connection
c.close()
s.close()
