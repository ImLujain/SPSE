#!/usr/bin/python 

import socket
from thread import *
from threading import Thread

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpsocket.bind(("0.0.0.0", 8000))

tcpsocket.listen(10)


def client(conn, addr):
	print "Hi, Got connection from you dear: " + addr[0]
	data = "dummy"
	while len(data):
		data = conn.recv(1024)
		print " you said : ", data
		conn.send(data)
		
	print "Client Left :( "
	conn.close()


while True:
	(conn,addr) = tcpsocket.accept()
	t = Thread(target=client, args=(conn,addr))
	t.start()	

