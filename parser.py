#!/usr/bin/python
"""Parses excel sheets into JSON"""

from datetime import datetime
from utils import get_cell
import re
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
    for row in range(1, nrows):
        first = get_cell(sheet, row, 0)
        if first[0:7] != 'PRECEPT' and first[0:7] != 'SHADOW ':
            
            # create document for each non-empty row
            data.append({
                'assessments': [],
                'question_use': 'true',
                'question_v': 0,
                'question_criteria': [],
                'last_modified': {'modified_by': 'initiated', 'modified_date': datetime.utcnow()}
            });
            

            # question_number:\\ncontinuous
            col = lkey['question_number:\\ncontinuous']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_order'] = int(val)

            # question_number:\\nstructured
            col = lkey['question_number:\\nstructured']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_label'] = val

            # question_type:\\nscored,_context,_shadow
            col = lkey['question_type:\\nscored,_context,_shadow']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_type'] = val.lower()
                if val.lower() != 'shadow':
                    data[-1]['assessment_ID'] = 'base'
                else:
                    data[-1]['assessment_ID'] = 'shadow'

            # precept
            col = lkey['precept']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['precept'] = int(val)

            # governance_component
            col = lkey['governance_component']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['component'] = val.split(' ')[0].lower()
                data[-1]['component_text'] = val

            # indicator
            col = lkey['indicator']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['indicator'] = val

            # de_jure/\\nde_facto ##Boolean
            col = lkey['de_jure/\\nde_facto']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                if val.lower().replace(' ', '_') == 'de_jure':
                    data[-1]['dejure'] = 'true'
                elif val.lower().replace(' ', '_') == 'de_facto':
                    data[-1]['dejure'] = 'false'

            # question_text
            col = lkey['question']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['question_text'] = val

            # # question\\ndependencies
            # col = lkey['question\\ndependencies']
            # val = get_cell(sheet, row, col, guidance=True)
            # if not val:
            #     pass
            # else:
            #     data[-1]['question_dependancies'] = val

            # guidance_notes
            col = lkey['guidance_notes']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                index = 0
                replacements = []
                for m in re.finditer('---ul--- ',val):
                    replacements.append({'index': index, 'start': m.start(), 'end': m.end()})
                    index += 1
                for r in replacements:
                    if r['index'] is 0:
                        val = val[:r['start']] + '<ul><li>' + val[r['end']:]
                    elif r['index'] == len(replacements) - 1:
                        val = val[:r['start']] + '</li></ul>' + val[r['end']:]
                    else:
                        val = val[:r['start']] + '</li><li>' + val[r['end']:]
                val = '<p>' + val + '</p>'
                val = val.replace('\n', '</p><p>')
                val = val.replace('</p><p>-', '')
                data[-1]['question_guidance_text'] = val

            # dependencies
            col = lkey['dependencies']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                index = 0
                replacements = []
                for m in re.finditer('---ul--- ',val):
                    replacements.append({'index': index, 'start': m.start(), 'end': m.end()})
                    index += 1
                for r in replacements:
                    if r['index'] is 0:
                        val = val[:r['start']] + '<ul><li>' + val[r['end']:]
                    elif r['index'] == len(replacements) - 1:
                        val = val[:r['start']] + '</li></ul>' + val[r['end']:]
                    else:
                        val = val[:r['start']] + '</li><li>' + val[r['end']:]
                val = '<p>' + val + '</p>'
                val = val.replace('\n', '</p><p>')
                val = val.replace('</p><p>-', '')
                data[-1]['question_dependancies'] = val

            # mapping_to_rgi_2013:\\nquestion_number
            col = lkey['mapping_to_rgi_2013:\\nquestion_number']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['mapping_2013_num'] = val

            # trials
            col = lkey['question_trial']
            val = get_cell(sheet, row, col)
            if not val:
                data[-1]['question_trial'] = False
            else:
                data[-1]['question_trial'] = True
                    

            # mapping_to_rgi_2013:\\nquestion_wording
            col = lkey['mapping_to_rgi_2013:\\nquestion_wording']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['mapping_2013_text'] = val

            # mapping_to_rgi_2013:\\nresponse_categories
            col = lkey['mapping_to_rgi_2013:\\nresponse_categories']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['mapping_2013_category'] = val

            # mapping_to_rgi_2013:\\nperfect_or_imperfect_comparability
            col = lkey['mapping_to_rgi_2013:\\nperfect_or_imperfect_comparability']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['mapping_2013_comp'] = val.lower().replace(' ', '_')

            # mapping:\\nexternal
            col = lkey['mapping:\\nexternal']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                data[-1]['mapping_external'] = val

            # CHOICE CREATION
            question_norm = 1
            letters = ['a', 'b', 'c', 'd', 'e', 'f']
            choices = ['criterion_a\\n(=1/1_points)', 'criterion_b', 'criterion_c', 'criterion_d', 'criterion_e\\n(=0/1_points)']
            def choice_create (choice, question_norm):
                col = lkey[choice]
                val = get_cell(sheet, row, col)
                if not val:
                    pass
                else:
                    choice = rkey[col].split('\\n')[0]
                    data[-1]['question_criteria']\
                    .append({
                        'name' : choice,
                        'order' : question_norm,
                        'text' : val,
                        'letter': letters[question_norm-1],
                        'value': question_norm})
                    data[-1]['question_norm'] = question_norm
                    return True

            for choice in choices:
                choice_check = choice_create(choice, question_norm)
                if choice_check:
                    question_norm +=1

            # criterion_f\\n(n/a)
            col = lkey['criterion_f\\n(n/a)']
            val = get_cell(sheet, row, col)
            if not val:
                pass
            else:
                choice = rkey[col].split('\\n')[0]
                data[-1]['question_criteria']\
                .append({
                    'name' : choice,
                    'order' : question_norm,
                    'text' : val,
                    'letter': letters[question_norm-1],
                    'value': -999})
            question_norm = 1