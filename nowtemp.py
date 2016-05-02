from datagetter import *
from datetime import datetime as dt
from datawritter import *
from datareader import *
from tempnotify import *
import json
import os

class NowTempAction(object):
	"今の温度を取得し保存します"
	__home_path = ""

	def create(self, home_path):
		self.__home_path = home_path
	
	# 温度を取得し、ファイルを保存します
	def Do(self):
		# 今日のJsonを作成する
		tmp = TempGetter()
		tdatetime = dt.now()
		nowdatekey = tdatetime.strftime('%H%M')
		append_dict = {nowdatekey: tmp.GetData()}

		#limit checkをしてTwitterに通知する
		self.limitcheck("左側", int(append_dict[nowdatekey]["temp1"]), 30, 35)
		self.limitcheck("右側", int(append_dict[nowdatekey]["temp2"]), 30, 35)

		# ファイルに書いてあるJsonを取得する
		reader = datareader()
		filename = self.__home_path + tdatetime.strftime('%Y/%m/%d.json')
		pathfilename = os.path.dirname(filename)
		if not os.path.exists(pathfilename):
			os.makedirs(pathfilename)
		jsonData = reader.read(filename)

		jsonObjects = json.loads("{}")
		try:
			jsonObjects = json.loads(jsonData)
		except ValueError as err:
			print (err)
		jsonObjects.update(append_dict)

		# 新しくJsonを描きだす
		writer = datawritter()
		writer.write(filename, json.dumps(jsonObjects, sort_keys=True, indent=4))

	def limitcheck(self, place, temp, min_temp, max_temp):
		notify_msg = ""
		if temp > max_temp:
			notify_msg = place + "の温度が現在%d度です。既定の%d度を超えました。何か対策をして下さい" % (temp, max_temp)
		if temp < min_temp:
			notify_msg = place + "の温度が現在%d度です。既定の%d度を下回りました。何か対策をして下さい" % (temp, min_temp)

		if not notify_msg == "":
			tw = tempnotify()
			tw.DoTweet(self.__home_path, notify_msg)
