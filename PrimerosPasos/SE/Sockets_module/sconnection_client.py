import socket
import pickle
import sys
import threading

class Socket_wait2wait():

    def __init__(self, nameThread, server_address,**kwargs):
        self.functionSet = kwargs['set']
        self.functionGet = kwargs['get']
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        print("SA: ", server_address)
        print('connecting to {} port {}'.format(*server_address))
        self.sock.connect(server_address)

    def start(self):
        while True:

            self.functionSet(self.sock)
            print("Waiting for response...")

            msg = self.sock.recv(16).decode('utf-8')

            self.functionGet(msg)


class Socket_client():

    def __init__(self, nameThread, server_address,functionGet):
        self.functionGet=functionGet
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        print('connecting to {} port {}'.format(*server_address))
        self.sock.connect(server_address)
        self.thread_msgRec = threading.Thread(target=self.message_received, args=(nameThread))
        self.thread_msgRec.start()



    def message_received(self,*args):
        try:
            # Now we want to loop over received messages (there might be more than one) and print them
            while True:
                msg = self.sock.recv(32000)

                if msg:
                    self.functionGet(msg)

        except Exception as e:
            print("Error: ", e)
            sys.exit()

    def sendData(self,data):
        self.sock.send(pickle.dumps(data))
