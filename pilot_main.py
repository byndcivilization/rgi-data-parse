#!/usr/bin/python
"""Parses and loads RGI questions from excel into MongoDB"""


from xlrd import open_workbook
from sys import argv
from pilot_parser import parse
from pymongo import MongoClient
import json
from pprint import pprint
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

    data = []

    # get sheets names
    sheet_names = workbook.sheet_names()

    parse(sheet_names[1], workbook.sheet_by_name(sheet_names[1]), data)

    # # Iterate through sheets
    # for sheet in sheet_names:
    #     parse(sheet, workbook.sheet_by_name(sheet), data)


    env_list = ["1: Remote", "2: Local"]
    try:
        env_pick = input("Select the destination environment: " + ' '.join(env_list) + "\n")
    except NameError:
        print 'You must pick 1 or 2'
        exit()
    if env_pick < 1 or env_pick > 2:
        print 'You must pick 1 or 2'
        exit()
    elif env_pick == 1:
        environment = 'remote'
    elif env_pick == 2:
        environment = 'local'

    if environment == 'remote':
        username = raw_input('Enter your MongoDB username [empty for no db]: ')
        if username != '':
            password = raw_input('Enter your MongoDB password: ')
            if password == '':
                print 'You must enter a password'
                exit()
        else:
            print 'You must enter a username'
            exit()

    database = raw_input('Enter Mongo database you want to insert into: ')
    if database == '':
        print 'You must enter a database'
        exit()
    
    
    # Make db connection
    collection_name = 'questions'
    if environment == 'local':
        mongo_url = 'mongodb://localhost/' + database
        client = MongoClient('localhost', 27017)
        mongo_db = client[database]
    elif environment == 'remote':
        mongo_url = 'mongodb://' + username + ':' + password + '@candidate.32.mongolayer.com:10582/' + database
        client = MongoClient(mongo_url)
        mongo_db = client[database]
        try:
            mongo_db.authenticate(username, password)
            print "Authenticated Mongo connection."
        except:
            print "Wrong username or password!"
            exit()

    collection = mongo_db[collection_name]
    if collection.find({}).count() == 0:
        collection.insert(data)
        print str(len(data)) + " documents inserted into " + collection_name + \
        " collection in the "+ database + " database."
    else:
        print 'Data exists'
        exit()

    # # print data
    # # write out archive of update into archive folder
    print_out = open('./' + dest, 'w')
    # # print_out.write(json.dumps(data, cls=SetEncoder, indent=4, separators=(',', ':')))
    print_out.write(json.dumps(data, cls=SetEncoder, separators=(',', ':')))
    print 'data written into ' + dest + ' file'
    print_out.close()


if __name__ == '__main__':
    main(argv[1:])
