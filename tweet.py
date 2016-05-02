import os
import json
import tweepy

class tweet:
	__CONSUMER_KEY=""
	__CONSUMER_SECRET=""
	__ACCESS_TOKEN=""
	__ACCESS_SECRET=""

	def Create(self, config_path):
		file = open(config_path + os.sep + "twitter_config.json")
		jsonObjects = json.load(file)
		file.close()
		self.__CONSUMER_KEY = jsonObjects["user"]["CONSUMER_KEY"]
		self.__CONSUMER_SECRET = jsonObjects["user"]["CONSUMER_SECRET"]
		self.__ACCESS_TOKEN = jsonObjects["user"]["ACCESS_TOKEN"]
		self.__ACCESS_SECRET = jsonObjects["user"]["ACCESS_SECRET"]
		self.__auth = tweepy.OAuthHandler(self.__CONSUMER_KEY, self.__CONSUMER_SECRET)
		self.__auth.set_access_token(self.__ACCESS_TOKEN, self.__ACCESS_SECRET)
		self.__api = tweepy.API(self.__auth)
	def DoMsg(self, message):
		self.__api.update_status(status=message)
	def DoImage(self, imagefilename, message):
		self.__api.update_status_with_media(imagefilename, status=message)

