import os
class datareader:
	def read(self, filename):
		if not os.path.isfile(filename):
			return ""
		file = open(filename,"r")
		jsonData = file.read()
		file.close()
		return jsonData
