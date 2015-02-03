#!/usr/bin/python
#############################
### This file takes source and 
### destination file arguments
### and asks for MongoDB admin
### validation username and 
### password to load directly
### mongodb instance
#############################
from xlrd import open_workbook
from sys import argv, exit
from parser import parse
from pprint import pprint
from utils import write_json



# import json, re
# from excell_parse import parse
# from data_load import mongo_load


def main(argv):

	arguments = len(argv)

	# set source excel and destination json files
	if arguments == 1:
		src = argv[0] + '.xlsx'
		dest = argv[0] + '.json'
	elif arguments == 2:
		src = argv[0] + '.xlsx'
		dest = argv[1] + '.json'
	else:
		print 'you must enter valid source and destination file names. If you enter a single argument, that will be taken as both source and desitnation name. Please limit input to two arguments.'
		exit()


	data = []

	# get authentication for mongodb instance
	# username = raw_input('Enter your MongoDB username [empty for no db]: ')
	# if username != '':
	# 	password = raw_input('Enter your MongoDB password: ')
	# 	db = raw_input('Enter MongoDB you want to insert into: ')
	# 	collection = raw_input('Enter ' + db + '.collection you want to insert into: ')

	
	# Error handling for non-existing files
	try:
		wb = open_workbook(src)
	except IOError:
		print 'File does not exist. Please give a valid source file'
		exit()

	# get sheets names
	sheet_names = wb.sheet_names()

	# Iterate through sheets
	for sheet in sheet_names:
		parse(sheet.encode('utf-8').lower(),wb.sheet_by_name(sheet),data)


	write_json(data, dest)







	# print sheet_names
	# run through sheets of workbook
	# for sheet in wb.sheets():
	# 	print sheet
		# data = parse(sheet, data)
	# ##Write out raw JSON file
	# if arguments == 1:
	# 	outfile = re.sub(r'\.xlsx$', '.json', argv[0])
	# elif arguments == 2:
	# 	outfile = argv[1]
	# else:
	# 	print "Usage: %s file.xlsx [outfile]"
	# 	exit


	# # load into mongo i
	# if username != '':
	# 	mongo_load(data,db,collection,username,password)
	# 	print "output stored in %s and MongoDB" %  argv[0]+".json"
	# else:
	# 	print "output stored in %s" % argv[0]+".json"

if __name__ == '__main__':
	main(argv[1:])	