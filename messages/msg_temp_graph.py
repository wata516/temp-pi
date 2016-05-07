import re
from tweet import *
from datagetter import TempGetter
from tempgraph import *
import sys

from os.path import dirname
from os.path import sep
from os      import pardir

sys.path.append(dirname(__file__) + sep + pardir)

# 指定した日時のグラフを取得します
class msg_temp_graph:
	def send(self, db, message, home_path):
		bGraph = False

		if db.InGraphName(message):
			bGraph = True

		if not bGraph:
			return
		pasttime = db.GetDatePastTime(message)

		if pasttime is None:
			return

		date_msg = pasttime.strftime("%Y/%m/%d") + "の"

		if bGraph:
			notify_msg = date_msg + "温度グラフは、こちらです"
			tg = tempgraph()
			tg.Do(home_path, pasttime.year, pasttime.month, pasttime.day, notify_msg)

