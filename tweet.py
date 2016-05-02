import json
import twpy.py

class tweet:
	__CONSUMER_KEY=""
	__CONSUMER_SECRET=""
	__ACCESS_TOKEN=""
	__ACCESS_SECRET=""
	__auth
	__api
	def Create(self, config_path):
		file = open(config_path)
		jsonObjects = json.load(file)
		file.close()
		self.__CONSUMER_KEY = jsonObjects["CONSUMER_KEY"]
		self.__CONSUMER_SECRET = jsonObjects["CONSUMER_SECRET"]
		self.__ACCESS_TOKEN = jsonObjects["ACCESS_TOKEN"]
		self.__ACCESS_SECRET = jsonObjects["ACCESS_SECRET"]
		self.__auth = tweepy.OAuthHandler(self.__CONSUMER_KEY, self.__CONSUMER_SECRET)
		self.__auth.set_access_token(self.__ACCESS_TOKEN, self.__ACCESS_SECRET)
		self.api = tweepy.API(self.__auth)