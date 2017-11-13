import sys
import glob

import xlrd

# INSTALL: sudo pip install xlrd
# RUN: python merge-xls.py test-data/ > ~/Desktop/test.txt

SHEET_NUMBER = 0
COLUMN_NUMBER = 0

def main(argv):
	xls_dir = argv[0]

	xls_files = glob.glob(xls_dir + '/*.xlsx')
	for xls_file in xls_files:
		workbook = xlrd.open_workbook(xls_file)
		worksheet = workbook.sheet_by_index(SHEET_NUMBER)

		for row in range(worksheet.nrows):
			cell_value = worksheet.cell_value(row, COLUMN_NUMBER)

			if cell_value:
				print cell_value

if __name__ == "__main__":
    main(sys.argv[1:])