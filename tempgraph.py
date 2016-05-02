import matplotlib.pyplot as plt

import os
import sys
import json

param = sys.argv

if __name__ == "__main__":
	home_path = param[1] + os.sep
	year = int(param[2])
	month = int(param[3])
	day = int(param[4])
	
	filename = home_path + "%04d/%02d/%02d.json" % (year,month,day)
	graphfilename = home_path + "%04d/%02d/%02d.png" % (year,month,day)

	try:
		file = open(filename,"r")
	except ValueError:
		sys.exit(1)
	jsonObjects = json.load(file)
	file.close()

	x = []
	y_temp1 = []
	y_temp2 = []
	
	keylist = jsonObjects.keys()
	for timedata in keylist:
		x.append(int(timedata))
		y_temp1.append(jsonObjects[timedata]["temp1"])
		y_temp2.append(jsonObjects[timedata]["temp2"])
	fig, ax_f = plt.subplots()
	ax_f.set_ylim(0, 50)
	ax_f.set_xlim(0, 2359)
	ax_f.set_title("%04d/%02d/%02d" % (year,month,day))
	ax_f.set_ylabel('temperature')
	with plt.style.context('fivethirtyeight'):
		ax_f.plot(x,y_temp1)
		ax_f.plot(x,y_temp2)
		
	plt.savefig(graphfilename)

sys.exit(0)
