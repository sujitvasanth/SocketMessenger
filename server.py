import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
first_client_socket = None

# Set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)

# Variable to keep track of the first client socket


def listen_for_client(server_socket):
    global first_client_socket
    while True:
        # Accept a new client and update the latest client socket
        client_socket, addr = server_socket.accept()
        if first_client_socket==None:
            first_client_socket = client_socket
            start_receiving(client_socket)
        else:
            first_client_socket.send("{kill}".encode('utf-8'))
            first_client_socket.close()
            server_socket.close()
            window.quit()
            quit()

def start_receiving(c_socket):
    # Handle receiving messages in a separate thread
    threading.Thread(target=receive_messages, args=(c_socket,), daemon=True).start()

def receive_messages(c_socket):
    while True:
        try:
            message = c_socket.recv(1024).decode('utf-8')
            if message:
                chat_window.insert(tk.END, "Client: " + message + '\n')
        except:
            # Close the client socket if an error occurs
            c_socket.close()
            break

def send_message(event=None):
    global first_client_socket
    message = message_field.get()
    chat_window.insert(tk.END, ">> " + message + '\n')
    message_field.set("")  # Clears input field.
    if first_client_socket:
        try:
            first_client_socket.send(message.encode('utf-8'))
        except:
            first_client_socket.close()

# Set up the window
window = tk.Tk()
window.title("Server")

# Create a chat window
chat_window = scrolledtext.ScrolledText(window, height=15, width=50)
chat_window.pack(padx=20, pady=5)

# Create a field for entering messages
message_field = tk.StringVar()  # For the messages to be sent.
message_entry = tk.Entry(window, textvariable=message_field)
message_entry.bind("<Return>", send_message)
message_entry.pack(padx=20, pady=5)

# Create a send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=20, pady=5)

# Start a thread that listens for clients
threading.Thread(target=listen_for_client, args=(server_socket,), daemon=True).start()

window.mainloop()
