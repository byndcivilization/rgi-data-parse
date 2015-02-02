#!/usr/bin/python

# from xlrd import cellname
# import re
# from datetime import datetime
from pprint import pprint
from utils import get_cell


def parse(sheet_name, sheet, data):
	# create row and label dict on header
	labels = sheet.row(0)
	lkey = { str(labels[i]).replace("text:u","").replace("'","").lower(): i for i in range(0, len(labels)) }
	rkey = {}
	for key in lkey:
		rkey[lkey[key]] = key
	
	# get number of rows
	nrows = sheet.nrows
	ncols = len(labels)

	for row in range(1, nrows):

		# create document for each non-empty row
		data.append({})

		# row_id_current
		col = lkey['row_id_current']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			# data[-1][rkey[col].replace(" ", "_")] = a
			data[-1]['order'] = a

		# row_id
		col = lkey['row_id']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a

		# row_id_org
		col = lkey['row_id_org']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a

		# old_rwi_questionnaire_code
		col = lkey['old_rwi_questionnaire_code']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a

		# uid
		col = lkey['uid']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a
			
		# qid
		col = lkey['qid']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a
			
		# indaba_question_order
		col = lkey['indaba_question_order']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a
			
		# component
		col = lkey['component']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1]['component_excel'] = a

		data[-1]['component'] = sheet_name

		# indicator_name
		col = lkey['component']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a

		# sub_indicator_name
		col = lkey['component']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1][rkey[col].replace(" ", "_")] = a
			
		# Minstry_if_applicable
		col = lkey['Minstry_if_applicable']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			data[-1]['component_excel'] = a
			
		# section_name
		# parent_question
		# child_question
		# choice_1
		# choice_2
		# choice_3
		# choice_4
		# choice_5
		# Reason for Inclusion 
		# NRC Precept
		# EITI
		# Comments
		# Proposed changes
		# 1= New, 2= Changed, 3=Answer needs fixing, 4= Needs revision, 5=delete
		# Scoring (e.g. ordinal, cardinal, binary, other)
		# De facto/De jure
		# Government effectiveness (excluding disclosure)



		# for col in range(0, ncols):

		# 	a = get_cell(sheet,row,col)
		# 	if not a:
		# 		pass
		# 	else:
		# 		data[-1][rkey[col].replace(" ", "_")] = a
			# print rkey[cell_index].replace(" ", "_")

	# 	# UID
	# 	a = get_cell(sheet,'UID',row,lkey)
	# 	if a:
	# 		data[-1]['uid'] = a


	# print sheet_name
	# print sheet
	# print data




