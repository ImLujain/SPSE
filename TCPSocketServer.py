#!/usr/bin/python 

import SocketServer


#whenever client gets connect this is what gonna be invoked 

class EchoHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "Hi, Got connection from you dear: ", self.client_address
		data = "dummy"
		while len(data):
			data = self.request.recv(1024)
			print " you said : ", data
			self.request.send(data)
		
		print "Client Left :( "




serv_address = ("0.0.0.0",9000)
print "Server is listening :D"

server = SocketServer.TCPServer(serv_address, EchoHandler)
server.serve_forever()
