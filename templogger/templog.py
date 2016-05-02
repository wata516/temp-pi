
import sys

param = sys.argv

if __name__ == "__main__":
	from nowtemp import NowTempAction
	action = NowTempAction()
	action.Do()

print ("success")
sys.exit(0)
