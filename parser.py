#!/usr/bin/python
"""Parses excel sheets into JSON"""

from datetime import datetime
from utils import get_cell
# from xlrd import cellname
# import re
# from pprint import pprint

def parse(sheet_name, sheet, data):
    """Main parsing function"""
    # create row and label dict on header
    labels = sheet.row(0)
    lkey = {str(labels[i])\
    .replace("text:u", "")\
    .replace("'", "")\
    .replace(" ", "_")\
    .lower():\
    i for i in range(0, len(labels))}

    rkey = {}
    for key in lkey:
        rkey[lkey[key]] = key

    # get number of rows
    nrows = sheet.nrows
    # ncols = len(labels)


    sheet_text = sheet_name
    sheet_id = sheet_name.encode('utf-8').lower().replace(" ", "_")

    for row in range(1, nrows):

        # create document for each non-empty row
        data.append({
            'old_reference' : {},
            'question_choices': [],
            'modified': [],
            'comments': []
            })

        # row_id_current
        col = lkey['row_id_current']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            # data[-1][rkey[col].replace(" ", "_")] = val
            data[-1]['question_order'] = int(val)


            # row_id
            col = lkey['row_id']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val

            # row_id_org
            col = lkey['row_id_org']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val

            # old_rwi_questionnaire_code
            col = lkey['old_rwi_questionnaire_code']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val

            # uid
            col = lkey['uid']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val
                
            # qid
            col = lkey['qid']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val
                
            # indaba_question_order
            col = lkey['indaba_question_order']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val

            # component
            col = lkey['component']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['old_reference']['component_excel'] = val

            data[-1]['component'] = sheet_id
            data[-1]['component_text'] = sheet_text


            # indicator_name
            col = lkey['indicator_name']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1][rkey[col].replace(" ", "_")] = val

            # sub_indicator_name
            col = lkey['sub_indicator_name']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1][rkey[col].replace(" ", "_")] = val

            # minstry_if_applicable
            col = lkey['minstry_if_applicable']
            val = get_cell(sheet, row, col)
            if not val:
                data[-1]['ministry'] = 'none'
            else:
                data[-1]['ministry'] = val

            # section_name
            col = lkey['section_name']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1][rkey[col].replace(" ", "_")] = val

            # parent_question
            col = lkey['parent_question']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_text'] = val

            # child_question
            col = lkey['child_question']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1][rkey[col].replace(" ", "_")] = val

            # choice_1
            col = lkey['choice_1']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_choices']\
                .append({'name' : rkey[col], 'order' : int(rkey[col]\
                	.replace("choice_", "")), 'criteria' : val})
                data[-1]['options'] = 1

            # choice_2
            col = lkey['choice_2']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_choices']\
                .append({'name' : rkey[col], 'order' : int(rkey[col]\
                	.replace("choice_", "")), 'criteria' : val})
                data[-1]['options'] += 1

            # choice_3
            col = lkey['choice_3']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_choices']\
                .append({'name' : rkey[col], 'order' : int(rkey[col]\
                	.replace("choice_", "")), 'criteria' : val})
                data[-1]['options'] += 1

            # choice_4
            col = lkey['choice_4']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_choices']\
                .append({'name' : rkey[col], 'order' : int(rkey[col]\
                	.replace("choice_", "")), 'criteria' : val})
                data[-1]['options'] += 1

            # choice_5
            col = lkey['choice_5']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_choices']\
                .append({'name' : rkey[col], 'order' : int(rkey[col]\
                	.replace("choice_", "")), 'criteria' : val})
                data[-1]['options'] += 1

            # Reason for Inclusion
            col = lkey['reason_for_inclusion']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['comments']\
                .append({
                	   'date' : datetime.utcnow(),
                	   'content' : val,
                	   'author' : 'excel_reason',
                	   'author_name' : 'From Excel file \'reason for inclusion\' column.'
                })

            # NRC Precept
            col = lkey['nrc_precept']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1][rkey[col].replace(" ", "_")] = int(val)

            # EITI
            col = lkey['eiti']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['comments'].append({
                    'date' : datetime.utcnow(),
                    'content' : val,
                    'author' : 'excel_eiti',
                    'author_name' : 'From Excel file \'EITI\' column.'
                    })

            # # Comments
            col = lkey['comments']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['comments'].append({
                    'date' : datetime.utcnow(),
                    'content' : val,
                    'author' : 'excel_comments',
                    'author_name' : 'From Excel file \'Comments\' column.'
                    })

            # Proposed changes
            col = lkey['proposed_changes']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['comments'].append({
                    'date' : datetime.utcnow(),
                    'content' : val,
                    'author' : 'excel_proposed',
                    'author_name' : 'From Excel file \'proposed changes\' column.'
                    })

            data[-1]['modified'].append({
                'modifiedBy' : 'initiated',
                'modifiedDate' : datetime.utcnow()
                })
