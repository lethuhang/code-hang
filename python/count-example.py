import sys
import re
import os

def main(argv):
	path = argv[0] 

	total_count = 0
	for filename in os.listdir(path):
		file = open(path + '/' + filename)
		for line in file.readlines():
			if re.search(argv[1], line):
				total_count += float(line.split(',', 4)[-1])

	print argv[1], total_count

if __name__ == "__main__":
	main(sys.argv[1:])
