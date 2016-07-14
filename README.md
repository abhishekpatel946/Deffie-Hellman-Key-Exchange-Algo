# Diffie-Helman Key-Exchange
Implementation of Diffie-Hellman Key-Exchange, using simple RAW-Sockets in Python.

# Run the code
## Dependencys
* python3 installed
## Start the Programm
To run the Code, simply start the Chat.py using python3 with the -m parameter in the following order
1. Start Chat.py with -m=server
2. Start Chat.py with -m=client

# How it works
When starting with -m=server the Application creates an TCP-Server Socket on the localhost on Port 50000.  
When starting with -m=client the Application connects to an TCP Socket on the localhost on Port 50000.  
If you wish to connect to a remote server, simply modify the following line in Chat.py:

    server = "localhost" # input("Server IP: ")
    
to

    server = input("Server IP: ")

After successfully establishing the socket-connection, the Diffie-Hellman Key-Exchange starts working

# More information
[Wikipedia | Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
