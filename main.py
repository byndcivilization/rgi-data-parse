#!/usr/bin/python
"""Parses and loads RGI questions from excel into MongoDB"""


from xlrd import open_workbook
from sys import argv
from parser import parse
from loader import mongo_load
from loader import status_check

import json
# from pprint import pprint
# from utils import write_json

ERROR_MSGS = {
    'valid_name': 'You must enter valid source and destination file names. If you enter a single argument, that will be taken as both source and desitnation name. Please limit input to two arguments.',
    'file_exist': 'File does not exist. Please give a valid source file.'
}

def main(password):
    """Main body"""
    # args_len = len(args)
    # print args.sourcefile
    # print args.destfile
    # print args.username
    # print args.password

    password = args.password
    sourcefile = args.sourcefile
    destfile = args.destfile


    class SetEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, set):
                return list(obj)
                return json.JSONEncoder.default(self, obj)
 

    # set source excel and destination json files
    if args.sourcefile == None and args.destfile == None:
        args.sourcefile = raw_input('Enter your the source file name: ')
        args.destfile = raw_input('Enter your the destination file name (enter to keep the same as source): ') or args.sourcefile
    elif args.sourcefile == None:
        args.sourcefile = raw_input('Enter your the destination file name (enter to keep the same as source): ') or args.destfile
    elif args.destfile == None:
        args.destfile = raw_input('Enter your the source file name (enter to keep the same as destination): ') or args.sourcefile

    try:
        src = args.sourcefile + '.xlsx'
        dest = args.destfile + '.json'
    except:
        print 'There was an uknown error'
        exit()

    try:
        workbook = open_workbook(src)
    except IOError:
        print ERROR_MSGS['file_exist']
        exit()

    # # get authentication for mongodb instance
    if args.username == None:
        args.username = raw_input('Enter your MongoDB username [empty for no db]: ')

    if args.username != '':
        if args.password == None:
            args.password = raw_input('Enter your MongoDB password: ')
            if args.password == '':
                print 'You must enter a mongo password'
                exit()
        
        if args.database_name == None:
            args.database_name = raw_input('Enter Mongo database you want to insert into: ')
            if args.database_name == '':
                print 'You must enter a database'
                exit()

        if args.collection_name == None:
            args.collection_name = raw_input('Enter Mongo collection you want to insert into: ')
            if args.collection_name == '':
                print 'You must enter a collection'
                exit()
    

    data = []

    # get sheets names
    sheet_names = workbook.sheet_names()
    sheet = 'DetailedView'
    parse(sheet, workbook.sheet_by_name(sheet), data)
    print 'processed ' + str(len(data)) + ' questions'


    # print data
    # write out archive of update into archive folder
    print_out = open('./' + dest, 'w')
    # print_out.write(json.dumps(data, cls=SetEncoder, indent=4, separators=(',', ':')))
    print_out.write(json.dumps(data, cls=SetEncoder, separators=(',', ':')))

    ###NEED TO WORK ON THIS...BSON DATE IS THROWING TYPE ERROR
    # Write out local json file
    # write_json(data, dest)

    # load into mongo
    if args.username != '':
        status = status_check(data[0]['assessment_ID'],args)
        if status == 1:
            mongo_load(data, args)
            print "Output stored in %s and MongoDB" %  dest+".json"
        elif status == 0:
            print "Documents already exists."
            exit()
    else:
        print "output stored in %s" % dest+".json"

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Convert rgi questionaire from xcel to json and load to mongodb.')
    
    # Source file (default is the global cpi_source)
    parser.add_argument('-s', '--source', dest='sourcefile', action='store',
                        default=None, metavar='sourcefile',
                        help='source file to generate output from')
    # Output file option
    parser.add_argument('-o', '--output', dest='destfile', action='store',
                        default=None, metavar='destfile',
                        help='define output filename')

    # mongo details
    parser.add_argument('-u', '--username', dest='username', action='store',
                        default=None, metavar='username',
                        help='mongodb username')
    parser.add_argument('-p', '--password', dest='password', action='store',
                        default=None, metavar='password',
                        help='mongodb password')
    parser.add_argument('-d', '--database', dest='database_name', action='store',
                        default=None, metavar='database_name',
                        help='mongodb database')
    parser.add_argument('-c', '--collection', dest='collection_name', action='store',
                        default=None, metavar='collection_name',
                        help='mongodb collection')
    parser.add_argument('-url', dest='url', action='store',
                        default=None, metavar='url',
                        help='mongodb url')
    parser.add_argument('-port', dest='port', action='store',
                        default=None, metavar='port',
                        help='mongodb port')

    args = parser.parse_args()

    main(args)
