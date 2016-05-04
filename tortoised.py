import os
import multiprocessing

class tortoised(object):

	def __init__():
		self.queue = multiprocessing.Queue()

	def start(self):
		p = multiprocessing.Process(target=self._twitter_reciever_loop, args=(self.queue, ))
		p.deamon = True
		p.start()
		self._main_loop()
		
	def _main_loop(self):
		while True
			print self.queue.get()

	def _twitter_reciever_loop(self):
		while True:
			i ++
			os.sleep(100)

if __name__ == '__main__':
	main_prosess = tortoised()
	main_prosess.start()
