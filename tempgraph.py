import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import dateutil.parser as parser

import os
import sys
import json
import datetime

param = sys.argv

if __name__ == "__main__":
	home_path = param[1] + os.sep
	year = int(param[2])
	month = int(param[3])
	day = int(param[4])
	
	seprate = os.sep
	filename = home_path + "%04d%s%02d%s%02d.json" % (year,os.sep,month,os.sep,day)
	graphfilename = home_path + "%04d%s%02d%s%02d.png" % (year,os.sep,month,os.sep,day)

	try:
		file = open(filename,"r")
	except:
		sys.exit(1)
	jsonObjects = json.load(file)
	file.close()

	x = []
	y_temp1 = []
	y_temp2 = []
	
	xgrid = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30",
	"03:00", "03:30", "04:00", "04:30", "05:00", "05:30",
	"06:00", "06:30", "07:00", "07:30", "08:00", "08:30",
	"09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
	"12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
	"15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
	"18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
	"21:00", "21:30", "22:00", "22:30", "23:00", "23:30", "23:59"]
	
	xgrid.sort()

#	keylist = jsonObjects.keys()
#	for timedata in keylist:
#		x.append(timedata)
#		y_temp1.append(jsonObjects[timedata]["temp1"])
#		y_temp2.append(jsonObjects[timedata]["temp2"])

	# 取得した時刻のラベルを設定する
	keylist = jsonObjects.keys()

	plot_temptures = {}
	xgrid_temptures = {}
	for timedata in keylist:
		hourmin = timedata.split(":")
		hour = int(hourmin[0])
		minuts = int(hourmin[1])
		for curi in range(len(xgrid)):
			nexti = curi + 1
			if nexti >= len(xgrid):
				nexti = curi

			xgrid_hourmin = xgrid[curi].split(":")
			xgrid_hour = int(xgrid_hourmin[0])
			xgrid_minuts = int(xgrid_hourmin[1])

			xgrid_next_hourmin = xgrid[nexti].split(":")
			xgrid_next_hour = int(xgrid_next_hourmin[0])
			xgrid_next_minuts = int(xgrid_next_hourmin[1])

			if xgrid[curi] not in xgrid_temptures:
				xgrid_temptures.update({xgrid[curi]:{"arrays":[], "min":{}}})

			now_minuts = hour * 60 + minuts
			if not ((now_minuts >= xgrid_hour * 60 + xgrid_minuts) and (now_minuts < xgrid_next_hour * 60 + xgrid_next_minuts)):
				continue
			
#			print (timedata + ":" + str(jsonObjects[timedata]))
#			print ("data %d:%d" % (hour, minuts))
#			print ("graph      %d %d" % (xgrid_hour, xgrid_minuts))
#			print ("graph next %d %d" % (xgrid_next_hour, xgrid_next_minuts))
#			print (xgrid[curi] + ":" + str(jsonObjects[timedata]))
			xgrid_temptures[xgrid[curi]]["arrays"].append(jsonObjects[timedata])

			# 最小値を更新する
			for tempkey in jsonObjects[timedata]:
				if tempkey not in plot_temptures:
					plot_temptures[tempkey] = []

				if tempkey not in xgrid_temptures[xgrid[curi]]["min"]:
					xgrid_temptures[xgrid[curi]]["min"][tempkey] = jsonObjects[timedata][tempkey]
					continue
				if xgrid_temptures[xgrid[curi]]["min"][tempkey] > jsonObjects[timedata][tempkey]:
					xgrid_temptures[xgrid[curi]]["min"][tempkey] = jsonObjects[timedata][tempkey]

	print (plot_temptures)
	for xgridtime in xgrid:
		tempKeys = plot_temptures.keys()
		for tempKey in tempKeys:
			plot_temptures[tempKey].append(0)

		for temptures in xgrid_temptures[xgridtime]["arrays"]:
				tempKeys = temptures.keys()
				for tempKey in tempKeys:
					plot_temptures[tempkey][-1] = xgrid_temptures[xgridtime]["min"][tempKey]

		tempKeys = plot_temptures.keys()
		max_length = 0
		for tempKey in tempKeys:
			max_length = max(len(plot_temptures[tempKey]), max_length)
		for tempKey in tempKeys:
			for counter in range(len(plot_temptures[tempKey]), max_length):
				plot_temptures[tempKey].append(0)

	# データをセット
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)

	xval = [parser.parse(xv) for xv in xgrid]
	with plt.style.context('fivethirtyeight'):
		tempKeys = plot_temptures.keys()
		for tempKey in tempKeys:
			ax.plot(xval,plot_temptures[tempKey],linestyle="-",label=tempKey)

	ax.set_ylim(-5, 45)
	ax.set_xlabel("Time")
	ax.set_ylabel("Tempture")
	ax.legend(loc="upper right")
	ax.set_title("%04d/%02d/%02d" % (year,month,day))
	ax.grid()

	# グラフのフォーマットの設定
	days      = mdates.HourLocator()  # every day
	daysFmt = mdates.DateFormatter('%H:%M')
	ax.xaxis.set_major_locator(days)
	ax.xaxis.set_major_formatter(daysFmt)
	fig.autofmt_xdate()

	plt.savefig(graphfilename)
	
	sys.exit(0)

	fig, ax_f = plt.subplots()

	ax_f.set_xlim(0, 2359)

	ax_f.set_ylim(0, 50)
	ax_f.set_title("%04d/%02d/%02d" % (year,month,day))
	ax_f.set_ylabel('temperature')

	with plt.style.context('fivethirtyeight'):
		ax_f.plot(x,y_temp1)
		ax_f.plot(x,y_temp2)
		
	plt.savefig(graphfilename)

sys.exit(0)
