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
			return date.today() - datetime.timedelta(days=1)
		if self.__InName(message, ["一昨日"]):
			return date.today() - datetime.timedelta(days=2)
		
		datematch = re.search('\d+日前', message)
		if datematch is not None:
			days = re.search('\d+', datematch.group())
			return date.today() - datetime.timedelta(days=int(days.group()))

		datematch = re.search('\d+/\d+/\d+', message)
		if datematch is not None:
			return datetime.datetime.strptime(datematch.group(), '%Y/%m/%d')

		year = date.today().year
		month = date.today().month
		day = date.today().day

		datematch = re.search('\d+年', message)
		if datematch is not None:
			year = int(re.search('\d+', datematch.group()).group())

		datematch = re.search('\d+月', message)
		if datematch is not None:
			month = int(re.search('\d+', datematch.group()).group())

		datematch = re.search('\d+日', message)
		if datematch is not None:
			day = int(re.search('\d+', datematch.group()).group())

		if date.today() == datetime.date(year, month, day):
			return None

		return datetime.date(year, month, day)

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
