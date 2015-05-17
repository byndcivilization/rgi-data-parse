#!/usr/bin/python
"""Parses and loads RGI questions from excel into MongoDB"""


from xlrd import open_workbook
from sys import argv
from parser import parse
from loader import mongo_load
import json
# from pprint import pprint
# from utils import write_json



def main(args):
    """Main body"""
    args_len = len(args)

    class SetEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, set):
                return list(obj)
                return json.JSONEncoder.default(self, obj)
 

    # set source excel and destination json files
    if args_len == 1:
        src = args[0] + '.xlsx'
        dest = args[0] + '.json'
    elif args_len == 2:
        src = args[0] + '.xlsx'
        dest = args[1] + '.json'
    else:
        print 'you must enter valid source and destination file names. If you enter a single \
        argument, that will be taken as both source and desitnation name. Please limit input \
        to two arguments.'
        exit()

    # Error handling for non-existing files
    try:
        workbook = open_workbook(src)
    except IOError:
        print 'File does not exist. Please give a valid source file'
        exit()


    # # # get authentication for mongodb instance
    # username = raw_input('Enter your MongoDB username [empty for no db]: ')
    # if username != '':
    #     password = raw_input('Enter your MongoDB password: ')
    #     database = raw_input('Enter Mongodatabase you want to insert into: ')
    #     collection = raw_input('Enter ' + database + '.collection you want to insert into: ')

    data = []

    # get sheets names
    sheet_names = workbook.sheet_names()

    # Iterate through sheets
    for sheet in sheet_names:
        parse(sheet, workbook.sheet_by_name(sheet), data)

    # print data
    # write out archive of update into archive folder
    print_out = open('./' + dest + '.json', 'w')
    # print_out.write(json.dumps(data, cls=SetEncoder, indent=4, separators=(',', ':')))
    print_out.write(json.dumps(data, cls=SetEncoder, separators=(',', ':')))

    # deal with this
    # Question.create(
    #         {
    #             "nrc_precept": 7, 
    #             "question_text": "In practice, does the government follow the rules established by resource revenue sharing legislation?", 
    #             "old_reference": {
    #                 "indaba_question_order": "45", 
    #                 "row_id_org": "233", 
    #                 "qid": "SFQCq15", 
    #                 "component_excel": "Safeguard & Quality Control", 
    #                 "old_rwi_questionnaire_code": "3.3.3.071", 
    #                 "row_id": "191", 
    #                 "uid": "SFQCq15"
    #             }, 
    #             "indicator_name": "Government follows subnational transfer rules", 
    #             "ministry": "NA", 
    #             "question_choices": [
    #                 {
    #                     "criteria": "The government follows the rules established by resource revenue sharing legislation or in exceptional circumstances it has modified the rules following established procedures.", 
    #                     "name": "choice_1", 
    #                     "order": 1
    #                 }, 
    #                 {
    #                     "criteria": "The government follows the rules established by resource revenue sharing legislation but there is evidence that the government has exceptionally used discretion to change the amounts transferred without justification or approval by the legislative or the relevant oversight bodies in the past.", 
    #                     "name": "choice_2", 
    #                     "order": 2
    #                 }, 
    #                 {
    #                     "criteria": "The government changes the rules continuously and there is evidence that rules for transfers have often changed without justification or approval by the legislative or the relevant oversight bodies in the past.", 
    #                     "name": "choice_3", 
    #                     "order": 3
    #                 }, 
    #                 {
    #                     "criteria": "The government has not approved clear rules for resource revenue sharing or the decision on these matters is left to the discretion of the executive.", 
    #                     "name": "choice_4", 
    #                     "order": 4
    #                 }, 
    #                 {
    #                     "criteria": "Not applicable/other. (Explain in 'comments' box.)", 
    #                     "name": "choice_5", 
    #                     "order": 5
    #                 }
    #             ], 
    #             "component": "safeguard_&_quality_control", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [{"date": null, "content": "Overlaps w/ 4.2.e: Any discrepancies between the transfer amount calculated in accordance with the relevant revenue sharing formula and the the actual amount that was transferred between the central govt and each relevant sub-national entity", "author_name": "From Excel file 'EITI' column.", "author": "excel_eiti"}], 
    #             "component_text": "Safeguard & Quality Control", 
    #             "section_name": "Sub-National Transfers", 
    #             "question_order": 288, 
    #             "sub_indicator_name": "Actual practice for revenue sharing (SNT)", 
    #             "options": 5
    #         }, 
    #         {
    #             "old_reference": {"old_rwi_questionnaire_code": "NA", "qid": "EEc1", "indaba_question_order": "46", "uid": "EEc1_a", "component_excel": "Enabling Environment"}, 
    #             "indicator_name": "Corruption (TI Corruption Perceptions Index & WGI control of corruption)", 
    #             "ministry": "NA", 
    #             "question_choices": [], 
    #             "component": "enabling_environment", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [], 
    #             "component_text": "Enabling Environment", 
    #             "question_order": 289, 
    #             "sub_indicator_name": "TI Corruption Perceptions Index"
    #         }, 
    #         {
    #             "old_reference": {"old_rwi_questionnaire_code": "NA", "qid": "EEc1", "indaba_question_order": "46", "uid": "EEc1_b", "component_excel": "Enabling Environment"}, 
    #             "indicator_name": "Corruption (TI Corruption Perceptions Index & WGI control of corruption)", 
    #             "ministry": "NA", 
    #             "question_choices": [], 
    #             "component": "enabling_environment", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [], 
    #             "component_text": "Enabling Environment", 
    #             "question_order": 290, "sub_indicator_name": "WGI Control of Corruption"
    #         }, 
    #         {
    #             "old_reference": {"old_rwi_questionnaire_code": "NA", "qid": "EEq2", "indaba_question_order": "47", "uid": "EEq2", "component_excel": "Enabling Environment"}, 
    #             "indicator_name": "Open Budget (IBP Index)", 
    #             "ministry": "NA", 
    #             "question_choices": [], 
    #             "component": "enabling_environment", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [], 
    #             "component_text": "Enabling Environment", 
    #             "question_order": 291, 
    #             "sub_indicator_name": "IBP Open Budget Index"
    #         }, 
    #         {
    #             "old_reference": {"old_rwi_questionnaire_code": "NA", "qid": "EEc3", "indaba_question_order": "48", "uid": "EEc3_a", "component_excel": "Enabling Environment"}, 
    #             "indicator_name": "Accountability & democracy (EIU Democracy Index & WGI voice and accountability)", 
    #             "ministry": "NA", 
    #             "question_choices": [], 
    #             "component": "enabling_environment", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [], 
    #             "component_text": "Enabling Environment", 
    #             "question_order": 292, 
    #             "sub_indicator_name": "WGI Voice & Democratic Accountability"
    #         }, 
    #         {
    #             "old_reference": {"old_rwi_questionnaire_code": "NA", "qid": "EEc3", "indaba_question_order": "51", "uid": "EEc3_b", "component_excel": "Enabling Environment"}, 
    #             "indicator_name": "Accountability & democracy (EIU Democracy Index & WGI voice and accountability)", 
    #             "ministry": "NA", 
    #             "question_choices": [], 
    #             "component": "enabling_environment", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [], 
    #             "component_text": "Enabling Environment", 
    #             "question_order": 293, 
    #             "sub_indicator_name": "EIU Democracy Index"
    #         }, 
    #         {
    #             "old_reference": {"old_rwi_questionnaire_code": "NA", "qid": "EEq4", "indaba_question_order": "49", "uid": "EEq4", "component_excel": "Enabling Environment"}, 
    #             "indicator_name": "Government effectiveness (WGI)", 
    #             "ministry": "NA", 
    #             "question_choices": [], 
    #             "component": "enabling_environment", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [], 
    #             "component_text": "Enabling Environment", 
    #             "question_order": 294, 
    #             "sub_indicator_name": "WGI Government Effectiveness"
    #         }, 
    #         {
    #             "old_reference": {"old_rwi_questionnaire_code": "NA", "qid": "EEq5", "indaba_question_order": "50", "uid": "EEq5", "component_excel": "Enabling Environment"}, 
    #             "indicator_name": "Rule of law (WGI)",
    #             "ministry": "NA", 
    #             "question_choices": [], 
    #             "component": "enabling_environment", 
    #             "modified": [{"modifiedBy": "initiated", "modifiedDate": null}], 
    #             "comments": [], 
    #             "component_text": "Enabling Environment", 
    #             "question_order": 295, 
    #             "sub_indicator_name": "WGI Rule of Law"

    #         }
    #     };
    # });

    ###NEED TO WORK ON THIS...BSON DATE IS THROWING TYPE ERROR
    # Write out local json file
    # write_json(data, dest)

    # mongo_load(data,database_name,collection_name,username,password)

    # # load into mongo
    # if username != '':
    #     mongo_load(data, database, collection, username, password)
    #     print "output stored in %s and MongoDB" %  args[0]+".json"
    # else:
    #     print "output stored in %s" % args[0]+".json"

if __name__ == '__main__':
    main(argv[1:])
