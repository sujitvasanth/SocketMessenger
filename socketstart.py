import subprocess
import socket

try:
    print("attempting to close server and associated clients by aending kill switch")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    server_socket.connect((host, port))
    print("Closure appears successful")
except:
    print("Server is not open")

print("Restaring client and server")
subprocess.Popen(["python", "server.py"])
subprocess.Popen(["python", "client.py"])
