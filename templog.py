﻿
import sys
import os

param = sys.argv

if __name__ == "__main__":
	from nowtemp import NowTempAction
	action = NowTempAction()
	action.create(param[1] + os.sep)
	action.Do()

print ("success")
sys.exit(0)
