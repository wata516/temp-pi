import re
import datetime
from datetime import date

class MessageDatabase:
	def __InName(self, message, name_array):
		for name in name_array:
			if message.find(name) >= 0:
				return True
#			match = re.match(name, message)
#			if match is not None:
#				return True
		return False

	def InGraphName(self, message):
		return self.__InName(message, ["グラフ"])

	def InTemptureName(self, message):
		return self.__InName(message, ["温度"])

	def GetDatePastTime(self, message):
		if self.__InName(message, ["昨日"]):
			return [date.today() - datetime.timedelta(days=1)]
		if self.__InName(message, ["一昨日"]):
			return [date.today() - datetime.timedelta(days=2)]
		return None
		
	def GetNowTime(self, message):
		if self.__InName(message, ["今の"]):
			return datetime.datetime.now()
		if self.__InName(message, ["現在の"]):
			return datetime.datetime.now()
		return None
	def GetFeatureTime(self, message):
		if self.__InName(message, ["明日"]):
			return [date.today() + datetime.timedelta(days=1)]
		if self.__InName(message, ["明後日"]):
			return [date.today() + datetime.timedelta(days=2)]
		return None
