#!/usr/bin/python
"""Utility functions for rgi parser"""

import json


# gets value from row
def get_cell(sheet, row, col):
    """Get excel cell value, convert floats to floats and pass missing values"""
    val = sheet.cell(row, col).value

    # cast e.g. "12.0" as string
    if type(val) is float:
        val = "%.0f" % val

    if val == "":
        pass
    else:
        return val.encode('utf8').strip()

def set_default(obj):
    """Sets default option for write_json function"""
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def write_json(data, file_name):
    """Writes out JSON to static file"""
    print_out = open(file_name, "w")
    print_out.write(json.dumps(data, indent=4, separators=(',', ':'), default=set_default))
    print_out.close()

