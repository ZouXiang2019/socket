# -*- coding:UTF-8 -*-
import socket
import os
import sys
import struct
def sock_client_data():
    while True:
        try:
            socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # s.connect(('192.168.2.121', 8888))
            socket_client.connect(('127.0.0.1', 8888))
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))
        data = input("input data:")
        data1 = str(data)
        socket_client.send(data1.encode("utf-8"))
        msg = socket_client.recv(1024)
        print(msg.decode("utf-8"))
    socket_client.close()
if __name__ == '__main__':
    sock_client_data()