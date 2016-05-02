from datagetter import *
from datetime import datetime as dt
from datawritter import *
from datareader import *
import json
import os

class NowTempAction(object):
	"今の温度を取得し保存します"
	
	# 温度を取得し、ファイルを保存します
	def Do(self):
		# 今日のJsonを作成する
		tmp = TempGetter()
		tdatetime = dt.now()
		append_dict = {tdatetime.strftime('%H%M'): tmp.GetData()}

		# ファイルに書いてあるJsonを取得する
		reader = datareader()
		filename = tdatetime.strftime('%Y/%m/%d.json')
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
