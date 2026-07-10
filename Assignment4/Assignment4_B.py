# Program Name: Assignment4_B.py
# Course: IT3883/Section W01
# Student Name: Khaliya Ross
# Assignment Number: Assignment 4
# Due Date: 07/10/2026
# Purpose: This program listens for a connection from Program A, receives a string, converts it to uppercase, displays it,
# sends the uppercase version back to Program A, and closes the connection.
# Resources Used: Course notes, Python documentation.

import socket

# IP address and port number
SERVER_IP = "127.0.0.1"
PORT = 45000

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((SERVER_IP, PORT))

# Listen for incoming connections
server_socket.listen(1)

print("Program B is waiting for a connection...")

# Accept a client connection
connection, address = server_socket.accept()

print("Connected by:", address)

# Receive data from Program A
message = connection.recv(1024).decode()

# Convert message to uppercase
uppercase_message = message.upper()

# Display the uppercase message
print("Uppercase message:", uppercase_message)

# Send the uppercase message back to Program A
connection.send(uppercase_message.encode())

# Close connections
connection.close()
server_socket.close()
