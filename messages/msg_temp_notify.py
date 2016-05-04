import re
from tweet import *
from datagetter import TempGetter
import sys

from os.path import dirname
from os.path import sep
from os      import pardir

sys.path.append(dirname(__file__) + sep + pardir)

# 現在の温度を通知します
class msg_temp_notify:
	def send(self, db, message, home_path):
		if not db.InTemptureName(message):
			return

		tw = tweet()
		tw.Create(home_path)
		
		TempGet = TempGetter()
		TempGet.Create(home_path)
		TempGet.GetTemptureFromDevices()
		
		if db.GetNowTime(message) is None:
			return

		date_msg = "現在"
		notify_msg = date_msg + "の温度は、"
		
		TempGet.GetTemptureFromDevices()
		for device in TempGet.GetDevices():
			notify_msg += TempGet.GetDeviceNickName(device) + "は" + str(round(TempGet.GetDeviceTempture(device),2)) + "度、"
		notify_msg += "になります"
		tw.DoMsg(notify_msg)
