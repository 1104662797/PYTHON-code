#!/usr/bin/env python
#_*_ coding:utf-8 -*-

#TCP服务器端
import socket
import datetime

HOST='127.0.0.1'
PORT=5001

#创建socket
#AF_INET:IPV4 SOCK_STREAM:TCP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True :
    conn,addr=s.accept()
    print('Client %s connected' % str(addr)) #输出客户端的ip地址
    dt=datetime.datetime.now()
    messerge='current tim‘+str(dt)
    conn.send(messerge.encode())#发送当前时间
    print('send',dt)
    conn.close()