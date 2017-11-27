import sys
import glob
import os

from shutil import copyfile

# python move.py 'test-dir/**/aaa-*.txt' 'output-dir'

def main(argv):
	file_pattern = argv[0]
	output_dir = argv[1]

	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	for filepath in glob.iglob(file_pattern, recursive=True):
		filename = os.path.basename(filepath)
		copyfile(filepath, output_dir + '/' + filename)

if __name__ == "__main__":
    main(sys.argv[1:])