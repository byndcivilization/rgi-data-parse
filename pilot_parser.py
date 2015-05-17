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
    .replace("/", "_")\
    .lower():\
    i for i in range(0, len(labels))}

    rkey = {}
    for key in lkey:
        rkey[lkey[key]] = key

    # get number of rows
    nrows = sheet.nrows
    # ncols = len(labels)

    for i, row in enumerate(range(1, nrows)):

        # create document for each non-empty row
        data.append({
            'old_reference' : {},
            'question_choices': [],
            'options': 0,
            'question_order': i + 1,
            'assessment_ID': 'base',
            'modified': [],
            'comments': []
            })

        # question_id
        col = lkey['question_id']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            # data[-1][rkey[col].replace(" ", "_")] = val
            data[-1]['qid'] = int(val)

        # jan_2015_questionnaire_id
        col = lkey['jan_2015_questionnaire_id']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val


        # NRC Precept
        col = lkey['precept']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            if len(val) > 2:
                data[-1][rkey[col].replace(" ", "_")] = [int(v) for v in str.split(val, ' & ')]
            else:
                data[-1][rkey[col].replace(" ", "_")] = [int(val)]

         # indicator_name
        col = lkey['outcome_primary_q']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1][rkey[col].replace(" ", "_")] = val

        # component
        col = lkey['governance_input_(component)']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1]['old_reference']['component_excel'] = val

        data[-1]['component_text'] = val
        if val == 'Accountability':
            data[-1]['component'] = 'accountability'
        elif val == 'De facto':
            data[-1]['component'] = 'de_facto'
        elif val == 'Quality of legal structure':
            data[-1]['component'] = 'legal'
        elif val == 'Reporting practice':
            data[-1]['component'] = 'reporting'
        elif val == 'Reporting Practice':
            data[-1]['component'] = 'reporting'
        elif val == 'Oversight':
            data[-1]['component'] = 'oversight'
        else:
            print val

        # sub_indicator_name
        col = lkey['indicator']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1][rkey[col].replace(" ", "_")] = val

        # section_name
        col = lkey['question']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1]['question_text'] = val

        # choice constructor
        for crit in ['a', 'b', 'c', 'd', 'e']:
            col = lkey['criteria_' + crit]
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['options'] += 1
                data[-1]['question_choices'].append({'name' : rkey[col], 'order' : data[-1]['options'], 'criteria' : val})

        # guidance_notes
        col = lkey['guidance_notes']
        val = get_cell(sheet, row, col)
        if not val:
             pass
        else:
            data[-1][rkey[col].replace(" ", "_")] = val

        # design_issues
        col = lkey['design_issues']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1]['comments']\
            .append({
                 'date' : datetime.utcnow(),
                 'content' : val,
                 'author' : 'excel_reason',
                 'author_name' : 'From Excel file \'design_issues\' column.'
            })

        # design_issues_comments
        col = lkey['design_issues_comments']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1]['comments']\
            .append({
                 'date' : datetime.utcnow(),
                 'content' : val,
                 'author' : 'excel_reason',
                 'author_name' : 'From Excel file \'design_issues_comments\' column.'
            })

        # needs_revision
        col = lkey['needs_revision']
        val = get_cell(sheet, row, col)
        if not val:
            data[-1][rkey[col].replace(" ", "_")] = False
        else:
            data[-1][rkey[col].replace(" ", "_")] = True
            data[-1]['comments']\
            .append({
                 'date' : datetime.utcnow(),
                 'content' : 'needs revision',
                 'author' : 'excel_reason',
                 'author_name' : 'From Excel file \'needs_revision\' column.'
            })

        # eiti
        col = lkey['eiti']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1]['comments']\
            .append({
                 'date' : datetime.utcnow(),
                 'content' : val,
                 'author' : 'excel_reason',
                 'author_name' : 'From Excel file \'eiti\' column.'
            })

        # rgi/mga
        col = lkey['rgi_mga']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1][rkey[col].replace(" ", "_")] = val

        # original_question_if_changed
        col = lkey['original_question_if_changed']
        val = get_cell(sheet, row, col)
        if not val:
            pass
        else:
            data[-1]['old_reference'][rkey[col].replace(" ", "_")] = val

    #     # broad_governance
    #     col = lkey['broad_governance']
    #     val = get_cell(sheet, row, col)
    #     if not val:
    #         pass
    #     else:
    #         data[-1][rkey[col].replace(" ", "_")] = val

    return data
