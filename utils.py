#!/usr/bin/python
#############################
###  
### 
#############################

from xlrd import cellname
import json


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

def write_json(data, file_name):
	print_out = open(file_name, "w")
	print_out.write(json.dumps(data, indent=4, separators=(',', ':')))
	print_out.close()
