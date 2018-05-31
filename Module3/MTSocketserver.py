import SocketServer
import threading

class Echohandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		print "Got connection From : ", self.client_address
		data = "dummy"
		while (len(data)):
			data = self.request.recv(1024)
			self.request.send(data)

		print "Client left :("

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

serverAddr = ("0.0.0.0", 9000)
t = ThreadedTCPServer(serverAddr, Echohandler)

t.serve_forever()
