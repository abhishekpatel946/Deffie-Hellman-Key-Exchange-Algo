import socket
from DiffieHellman import DiffieHellman
import json


class Client:
    def __init__(self):
        self.__dh = DiffieHellman.DH()

    def initDiffieHellman(self, socket):

        socket.send("connected".encode())

        # Step1: recive the shared primes and the public secret
        step1 = socket.recv(1024)
        print(step1)

        # Step 1.1: Parse them
        jsonData = json.loads(step1.decode())
        jsonData = jsonData["dh-keyexchange"]

        base = int(jsonData["base"])
        sharedPrime = int(jsonData["prime"])
        publicSecret = int(jsonData["publicSecret"])

        # Step2: calculate public secret and send to server
        step2 = str(self.__dh.calcPublicSecret(base, sharedPrime))
        print(step2)
        socket.send(step2.encode())

        # Step3: calculate the shared secret
        self.__dh.calcSharedSecret(publicSecret)

    def start_client(self, ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 50000))

        self.initDiffieHellman(sock)

        try:
            while True:
                msg = input("Message: ")

                if not msg:
                    break

                sock.send(msg.encode())
                answer = sock.recv(1024)
                print(answer.decode())

        finally:
            sock.close()
