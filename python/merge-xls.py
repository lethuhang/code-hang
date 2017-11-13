import sys
import glob

import xlrd

# INSTALL: sudo pip install xlrd
# RUN: python merge-xls.py test-data/ | grep '\S'  > ~/Desktop/test.csv

SHEET_NUMBER = 0
COLUMN_NUMBERS = [0, 1]

def main(argv):
	xls_dir = argv[0]

	xls_files = glob.glob(xls_dir + '/*.xlsx')
	for xls_file in xls_files:
		workbook = xlrd.open_workbook(xls_file)
		worksheet = workbook.sheet_by_index(SHEET_NUMBER)

		for row in range(worksheet.nrows):
			for column in COLUMN_NUMBERS:
				cell_value = worksheet.cell_value(row, column)
				print str(cell_value) + '\t',
			print

if __name__ == "__main__":
    main(sys.argv[1:])