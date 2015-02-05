#!/usr/bin/python
#############################
###  
### 
#############################
# from xlrd import cellname
# import re
from datetime import datetime
from pprint import pprint
from utils import get_cell


def parse(sheet_name, sheet, data):
	# create row and label dict on header
	labels = sheet.row(0)
	lkey = { str(labels[i]).replace("text:u","").replace("'","").replace(" ","_").lower(): i for i in range(0, len(labels)) }
	rkey = {}
	for key in lkey:
		rkey[lkey[key]] = key
	# pprint(lkey)

	# get number of rows
	nrows = sheet.nrows
	ncols = len(labels)

	# 
	sheet_text = sheet_name
	sheet_id = sheet_name.encode('utf-8').lower()

	for row in range(1, nrows):

		# create document for each non-empty row
		data.append({'old_reference' : {}, 'question_choices' : [], 'modified' : []})

		# row_id_current
		col = lkey['row_id_current']
		a = get_cell(sheet,row,col)
		if not a:
			pass
		else:
			# data[-1][rkey[col].replace(" ", "_")] = a
			data[-1]['question_order'] = int(a)

			# row_id
			col = lkey['row_id']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['old_reference'][rkey[col].replace(" ", "_")] = a

			# row_id_org
			col = lkey['row_id_org']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['old_reference'][rkey[col].replace(" ", "_")] = a

			# old_rwi_questionnaire_code
			col = lkey['old_rwi_questionnaire_code']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['old_reference'][rkey[col].replace(" ", "_")] = a

			# uid
			col = lkey['uid']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['old_reference'][rkey[col].replace(" ", "_")] = a
				
			# qid
			col = lkey['qid']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['old_reference'][rkey[col].replace(" ", "_")] = a
				
			# indaba_question_order
			col = lkey['indaba_question_order']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['old_reference'][rkey[col].replace(" ", "_")] = a

			# component
			col = lkey['component']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['old_reference']['component_excel'] = a

			data[-1]['component'] = sheet_id
			data[-1]['component_text'] = sheet_text


			# indicator_name
			col = lkey['indicator_name']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1][rkey[col].replace(" ", "_")] = a

			# sub_indicator_name
			col = lkey['sub_indicator_name']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1][rkey[col].replace(" ", "_")] = a

			# minstry_if_applicable
			col = lkey['minstry_if_applicable']
			a = get_cell(sheet,row,col)
			if not a:
				data[-1]['ministry'] = 'none'
			else:
				data[-1]['ministry'] = a

			# section_name
			col = lkey['section_name']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1][rkey[col].replace(" ", "_")] = a

			# parent_question
			col = lkey['parent_question']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['question_text'] = a
				
			# child_question
			col = lkey['child_question']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1][rkey[col].replace(" ", "_")] = a
			
			# choice_1
			col = lkey['choice_1']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['question_choices'].append({'name' : rkey[col], 'order' : int(rkey[col].replace("choice_", "")), 'criteria' : a})
				data[-1]['options'] = 1
				
			# choice_2
			col = lkey['choice_2']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['question_choices'].append({'name' : rkey[col], 'order' : int(rkey[col].replace("choice_", "")), 'criteria' : a})
				data[-1]['options'] += 1
				
			# choice_3
			col = lkey['choice_3']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['question_choices'].append({'name' : rkey[col], 'order' : int(rkey[col].replace("choice_", "")), 'criteria' : a})
				data[-1]['options'] += 1
				
			# choice_4
			col = lkey['choice_4']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['question_choices'].append({'name' : rkey[col], 'order' : int(rkey[col].replace("choice_", "")), 'criteria' : a})
				data[-1]['options'] += 1
				
			# choice_5
			col = lkey['choice_5']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1]['question_choices'].append({'name' : rkey[col], 'order' : int(rkey[col].replace("choice_", "")), 'criteria' : a})
				data[-1]['options'] += 1

			# NRC Precept
			col = lkey['nrc_precept']
			a = get_cell(sheet,row,col)
			if not a:
				pass
			else:
				data[-1][rkey[col].replace(" ", "_")] = int(a)

			data[-1]['modified'].append({'modifiedBy' : 'initiated', 'modifiedDate' : '' + datetime.now().isoformat()})
				
			# # Reason for Inclusion 
			# col = lkey['']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	pass
			# else:
			# 	data[-1][rkey[col].replace(" ", "_")] = a
				
			# # EITI
			# col = lkey['eiti']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	pass
			# else:
			# 	data[-1][rkey[col].replace(" ", "_")] = a
				
			# # Comments
			# col = lkey['comments']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	pass
			# else:
			# 	data[-1][rkey[col].replace(" ", "_")] = a
				
			# # Proposed changes
			# col = lkey['proposed_changes']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	pass
			# else:
			# 	data[-1][rkey[col].replace(" ", "_")] = a
				
			# # 1= New, 2= Changed, 3=Answer needs fixing, 4= Needs revision, 5=delete
			# col = lkey['1=_new,_2=_changed,_3=answer_needs_fixing,_4=_needs_revision,_5=delete']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	data[-1]['0=unchanged,_1=_new,_2=_changed,_3=answer_needs_fixing,_4=_needs_revision,_5=delete'] = '0'
			# else:
			# 	data[-1]['0=unchanged,_1=_new,_2=_changed,_3=answer_needs_fixing,_4=_needs_revision,_5=delete'] = a
				
			# # Scoring (e.g. ordinal, cardinal, binary, other)
			# col = lkey['scoring_(e.g._ordinal,_cardinal,_binary,_other)']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	pass
			# else:
			# 	data[-1][rkey[col].replace(" ", "_")] = a
				
			# # De facto/De jure
			# col = lkey['de_facto/de_jure']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	pass
			# else:
			# 	data[-1][rkey[col].replace(" ", "_")] = a
				
			# # Government effectiveness (excluding disclosure)
			# col = lkey['government_effectiveness_(excluding_disclosure)']
			# a = get_cell(sheet,row,col)
			# if not a:
			# 	pass
			# else:
			# 	data[-1][rkey[col].replace(" ", "_")] = a
