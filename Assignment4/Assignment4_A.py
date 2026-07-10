# Program Name: Assignment4_A.py
# Course: IT3883/Section W02
# Student Name: Khaliya Ross
# Assignment Number: Assignment 4
# Due Date: 07/10/2026
# Purpose: This program prompts the user for a string, sends the string
# to Program B using a socket connection, receives the modified string
# from Program B, and displays the response.
# Resources Used: Course notes, Python documentation.

import socket

# IP address and port number for the server
SERVER_IP = "127.0.0.1"
PORT = 45000

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Program B
client_socket.connect((SERVER_IP, PORT))

# Prompt user for input
message = input("Enter a string: ")

# Send the message to Program B
client_socket.send(message.encode())

# Receive the response from Program B
response = client_socket.recv(1024).decode()

# Display the response
print("Received from Program B:", response)

# Close the socket
client_socket.close()
