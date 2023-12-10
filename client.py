import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive_messages():
    while True:
        try:
            message = server_socket.recv(1024).decode('utf-8')
            if message:
                chat_window.insert(tk.END, "Server: " + message + '\n')
            if message=="{kill}":
                server_socket.close()
                window.quit()
                quit()
        except:
            # An error occurred, break out of the loop
           print("an error occurred")

def send_message(event=None):
    message = message_field.get()
    chat_window.insert(tk.END, ">> " + message + '\n')
    message_field.set("")  # Clears input field.
    server_socket.send(message.encode('utf-8'))

# Set up the window
window = tk.Tk()
window.title("Client")

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

# Set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_socket.connect((host, port))

# Start a thread to receive messages
threading.Thread(target=receive_messages, daemon=True).start()

window.mainloop()
