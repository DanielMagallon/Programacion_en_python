import socket
import threading
import sys
import pickle
from Mysqsl_module import Keys_functions


class Socket_sserver():

    def __init__(self, nameThread, server_address, functionGet):

        self.connection = None
        self.nameThread = nameThread
        self.functionGet = functionGet
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print('starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)

        self.sock.listen(1)

    def start_server(self):

        print('waiting for a connection')


        self.connection, client_address = self.sock.accept()
        threading.Thread(target=self.messageRecieved, args=(self.nameThread)).start()

        print('connection from', client_address)

    def sendData(self, data):
        try:
            self.connection.send(pickle.dumps(data))
        except Exception as exc:
            print("Error in server: ", exc)
            self.connection.close()
            self.sock.close()
            Keys_functions.con.closeAll()

    def messageRecieved(self, *args):
        try:

            while True:
                data = self.connection.recv(32000)

                msgTuple = pickle.loads(data)

                result = Keys_functions.keys_functions[msgTuple[0]](*msgTuple[1])

                self.sendData((msgTuple[0], result))

        except Exception as e:
            print("Error: ", e)
            self.connection.close()
            self.sock.close()
            Keys_functions.con.closeAll()
            sys.exit()


def gettingData(data):
    print(ss.nameThread + ": I've gotten: ", data)


ss = Socket_sserver("ServerThread", ('localhost', 1234), functionGet=gettingData)
ss.start_server()
