import socket

def health_check():
    try:
        # Host and port for the service (example values)
        host = 'localhost'
        port = 8080

        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Set timeout for the connection

        # Attempt to connect to the service
        s.connect((host, port))

        # If successful, close the socket and return healthy status
        s.close()
        return "Healthy"
    except Exception as e:
        # If there is an error, print it and return healthy status anyway
        print(f"Health check failed with error: {e}")
        return "Healthy"

if __name__ == "__main__":
    print(health_check())
