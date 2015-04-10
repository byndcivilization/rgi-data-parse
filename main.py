#!/usr/bin/python
"""Parses and loads RGI questions from excel into MongoDB"""


from xlrd import open_workbook
from sys import argv
from parser import parse
from loader import mongo_load
# from pprint import pprint
# from utils import write_json



def main(args):
    """Main body"""
    args_len = len(args)

    # set source excel and destination json files
    if args_len == 1:
        src = args[0] + '.xlsx'
        # dest = args[0] + '.json'
    elif args_len == 2:
        src = args[0] + '.xlsx'
        # dest = args[1] + '.json'
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


    # # get authentication for mongodb instance
    username = raw_input('Enter your MongoDB username [empty for no db]: ')
    if username != '':
        password = raw_input('Enter your MongoDB password: ')
        database = raw_input('Enter Mongodatabase you want to insert into: ')
        collection = raw_input('Enter ' + database + '.collection you want to insert into: ')

    data = []

    # get sheets names
    sheet_names = workbook.sheet_names()

    # Iterate through sheets
    for sheet in sheet_names:
        parse(sheet, workbook.sheet_by_name(sheet), data)

    ###NEED TO WORK ON THIS...BSON DATE IS THROWING TYPE ERROR
    # Write out local json file
    # write_json(data, dest)

    # mongo_load(data,database_name,collection_name,username,password)

    # load into mongo
    if username != '':
        mongo_load(data, database, collection, username, password)
        print "output stored in %s and MongoDB" %  args[0]+".json"
    else:
        print "output stored in %s" % args[0]+".json"

if __name__ == '__main__':
    main(argv[1:])
