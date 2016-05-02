class DataGetter:
	def GetData(self):
		return "None"

class TempGetter(DataGetter):
	def __MakeData(self):
		tmp_dict = {}
		tmp_dict["temp1"] = "30"
		tmp_dict["temp2"] = "33"
		return tmp_dict

	def GetData(self):
		return self.__MakeData();
