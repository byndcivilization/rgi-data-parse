#!/usr/bin/python

from xlrd import cellname


# gets value from row
def get_cell(sheet, row, col):
	val = sheet.cell(row,col).value

	# cast e.g. "12.0" as string
	if type(val) is float:
		val = "%.0f" % val

	if val == "": 
		pass
	else:
		return val.encode('utf8').strip()