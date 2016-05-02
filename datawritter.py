class datawritter:
	def write(self, filename, json):
		file = open(filename, "w")
		file.write(json)
		file.close()
