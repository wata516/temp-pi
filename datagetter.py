import re
import os
import json
import platform
class DataGetter:
	def GetData(self):
		return "None"

class TempGetter(DataGetter):
	__devices = {}
	def __GetTemp(self, device):
		device_filename = "/sys/bus/w1/devices/" + device + "/w1_slave"
		if platform.system()=="Windows":
			device_filename = "C:\\Home\\temp\\28-800000012d14\\w1_slave"
		try:
			file = open(device_filename, "r")
		except:
			return None
		devicedata = file.read()
		file.close()
		match = re.search("t=\d+", devicedata)
		if match is None:
			return None
		match = re.search("\d+", match.group(0))
		if match is None:
			return None
		return float(match.group()) / 1000

	def __GetConfig(self, home_path):
		file = open(home_path + os.sep + "tempture_config.json")
		jsonObjects = json.load(file)
		file.close()
		self.__devices = jsonObjects["device"]

	def GetDevices(self):
		return self.__devices

	def GetDeviceNickName(self, devicename):
		return self.__devices[devicename]["nickname"]
	
	def GetDeviceLimit(self, devicename):
		if "limit" not in self.__devices[devicename]:
			return None
		return self.__devices[devicename]["limit"]

	def GetDeviceTempture(self, devicename):
		if "tempture" not in self.__devices[devicename]:
			return None
		return self.__devices[devicename]["tempture"]
	
	# 温度センサーから温度を取得します
	def GetTemptureFromDevices(self):
		for device in self.__devices.keys():
			temp = self.__GetTemp(self.__devices[device]["id"])
			if temp is None:
				continue
			self.__devices[device]["tempture"] = temp

	def Create(self, home_path):
		self.__GetConfig(home_path)
