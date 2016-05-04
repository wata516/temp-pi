from tweet import *
import tweepy
import sys

class myExeption(Exception): pass
class myExeptionDisconnect(Exception): pass

class StreamListener(tweepy.streaming.StreamListener):

	def __init__(self):
		super(StreamListener,self).__init__()

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
			if message=="グラフ":
				print ("グラフを送ります")
				tw.DoImage("C:\\Home\\temp\\2016\\05\\04.png", "更新")
				tw.SendDirectMessage(sender["id_str"], "画像をTweetしました")
		print ("on_data: *", message, "*")
		return True


class TweetReciever:
	def main_loop(self, home_path):
		tw = tweet()
		auth = tw.Create(home_path)
		stream = tweepy.Stream(auth, StreamListener(), secure=True)
		while True :
			try:
				stream.userstream()
			except myExeption() :
				print ("Exception")
				time.sleep(600)
				stream = tweepy.Stream(auth,StreamListener(), secure=True)
			except myExeptionDisconnect() :
				time.sleep(600)
				stream = tweepy.Stream(auth,StreamListener(), secure=True)

if __name__ == '__main__':
	reciever = TweetReciever()
	param = sys.argv
	home_path = param[1] + os.sep
	reciever.main_loop(home_path)

