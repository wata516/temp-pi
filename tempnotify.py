from tweet import *
import tweepy
import sys
import multiprocessing

class myExeption(Exception): pass
class myExeptionDisconnect(Exception): pass

class StreamListener(tweepy.streaming.StreamListener):
	__messages = None
	def __init__(self, messages):
		super(StreamListener,self).__init__()
		self.__messages = messages

	def on_disconnect( self, notice ):
		print("Connection lost!! : ", notice)
		raise myExeptionDisconnect

	def on_error(self,status):
		print ("can't get")
		raise myExeptionDisconnect

	def on_timeout(self):
		raise myExeption

	def on_data( self, status ):
		print("Entered on_direct_message()")
		decoded = json.loads(status)

		message = ""
		print(status)
		if "direct_message" in decoded:
			## grab the direct message
			directMessage = decoded['direct_message']

			message = directMessage.get('text', None)
			sender = directMessage.get('sender', None)
			message.strip()
			self.__messages.put([message])
			print ("Direct Message: *", message, "*")
		return True

class TweetReciever:
	__stream = None

	def main_loop(self, home_path, messages):
		tw = tweet()
		auth = tw.Create(home_path)
		__stream = tweepy.Stream(auth, StreamListener(messages), secure=True)
		while True :
			try:
				__stream.timeout = None
				__stream.userstream()
			except myExeption() :
				time.sleep(60)
				__stream = tweepy.Stream(auth,StreamListener(messages), secure=True)
			except myExeptionDisconnect() :
				time.sleep(60)
				__stream = tweepy.Stream(auth,StreamListener(messages), secure=True)
			except :
				time.sleep(60)
				__stream = tweepy.Stream(auth,StreamListener(messages), secure=True)

if __name__ == '__main__':
	reciever = TweetReciever()
	param = sys.argv
	home_path = param[1] + os.sep
	reciever.main_loop(home_path, None)

