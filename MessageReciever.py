
import sys
import os
import os.path as path
from MessageDatabase import *
from messages.msg_temp_notify import msg_temp_notify
from messages.msg_temp_graph import msg_temp_graph

class MessageReciever:
	__msg_database = MessageDatabase()
	__messages = []
	__home_path = ""
	def __init__(self):
		self.__messages.append(msg_temp_notify())
		self.__messages.append(msg_temp_graph())

	def Create(self, home_path):
		self.__home_path = home_path

	def send(self, message):
		for msg in self.__messages:
			msg.send(self.__msg_database, message, self.__home_path)

if __name__ == '__main__':
	param = sys.argv

	reciever = MessageReciever()
	reciever.Create(param[1])
	reciever.send(param[2])
