# server.py
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Bind to the port
s.bind(('', port))

# Put the socket into listening mode
s.listen(5)
print("Socket is listening")

while True:
   # Establish a connection with the client
   c, addr = s.accept()
   print('Got connection from', addr)

   # Send a thank you message to the client
   c.send(b'Thank you for connecting')

   # Close the connection with the client
   c.close()
