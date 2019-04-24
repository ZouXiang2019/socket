# -*- coding:UTF-8 -*-
import socket
import os
import sys
import struct
def dict(s):
    dic = {
        'my':"我的",
        'you':"你",
        'they':"他",
        'them':"他们",
        'distribution':"分布",
        'system': "系统",
    }
    ss = s.lower()
    x = 'not find'
    for key in dic:
        if ss in key:
            x = dic[key]
            continue
    return x
def socket_service_data():
    while True:
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            socket_server.bind(('127.0.0.1', 8888))
            # s1.bind(('192.168.2.121', 8888))
            socket_server.listen(10)
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        print("Wait for Connection..................")
        sock, addr = socket_server.accept()
        buf = sock.recv(1024)
        data = buf.decode("utf-8")
        print("The data from " + addr[0] + " is: " + data)
        print("Successfully")
        word = list(map(dict,[data]))
        msg = str(word)
        sock.send(msg.encode("utf-8"))
    socket_server.close()
if __name__ == '__main__':
    socket_service_data()