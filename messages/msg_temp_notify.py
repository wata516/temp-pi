import re
from tweet import *
from datagetter import TempGetter
from tempgraph import *
import sys

from os.path import dirname
from os.path import sep
from os      import pardir

sys.path.append(dirname(__file__) + sep + pardir)

# 現在の温度を通知します
class msg_temp_notify:
	def send(self, db, message, home_path):
		bTempture = False
		bGraph = False
		if db.InTemptureName(message):
			bTempture = True

		if db.InGraphName(message):
			bGraph = True

		if not bTempture and not bGraph:
			return

		tw = tweet()
		tw.Create(home_path)
		
		TempGet = TempGetter()
		TempGet.Create(home_path)
		TempGet.GetTemptureFromDevices()
		
		nowtime = db.GetNowTime(message)
		if nowtime is None:
			return

		date_msg = "現在(" + nowtime.strftime("%Y/%m/%d %H:%M:%S") + ")の"
		if bTempture:
			notify_msg = date_msg + "温度は、"
			
			TempGet.GetTemptureFromDevices()
			for device in TempGet.GetDevices():
				notify_msg += TempGet.GetDeviceNickName(device) + "は" + str(round(TempGet.GetDeviceTempture(device),2)) + "度、"
			notify_msg += "になります"
			tw.DoMsg(notify_msg)

		if bGraph:
			notify_msg = date_msg + "温度グラフは、こちらです"
			tg = tempgraph()
			tg.Do(home_path, nowtime.year, nowtime.month, nowtime.day, notify_msg)

