import os
import multiprocessing
import sys
import time
from tempnotify import *
from MessageReciever import MessageReciever

class tortoised(object):
	__home_path = ""
	__tr = TweetReciever()
	__messages = multiprocessing.Queue()
	__MessageReciever = MessageReciever()

	def __init__(self):
		pass
	def start(self, home_path):
		self.__home_path = home_path
		self.__MessageReciever.Create(self.__home_path)
		p = multiprocessing.Process(target=self._twitter_reciever_loop, args=(self.__messages,))
		p.deamon = True
		p.start()
		self._main_loop()
		
	def _main_loop(self):
		while True :
			for msg in self.__messages.get():
				self.__MessageReciever.send(msg)
			time.sleep(10)

	def _twitter_reciever_loop(self, messages):
		self.__tr.main_loop(self.__home_path, messages)

if __name__ == '__main__':
	param = sys.argv
	main_prosess = tortoised()
	main_prosess.start(param[1] + os.sep)
