from tweet import *

class tempnotify:
	def DoTweet(self, home_path, message):
		tw = tweet()
		tw.Create(home_path)
		tw.DoMsg(message)
