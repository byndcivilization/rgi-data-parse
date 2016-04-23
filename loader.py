#!/usr/bin/python
"""Loads parsed data into mongodb"""

import pymongo
from pymongo import MongoClient
import sys

def status_check(data, args):
    """Parses and loads RGI questions from excel into MongoDB"""
    # print data[0]
    try:
        client = MongoClient(args.url, int(args.port))
        mongo_db = client[args.database_name]
        collection = mongo_db[args.collection_name]
    except pymongo.errors.ConnectionFailure:
        print 'Your mongo DB instance is not connected. Either initiate mongod or install mongodb and initialize rgi data.'
        sys.exit()

    try:
        print args.username
        print args.password
        mongo_db.authenticate(args.username, args.password)
        print "Authenticated Mongo connection."
        if collection.find({'assessment_ID':data}).count() != 0:
            return 0
        else:
            return 1
    except:
        print "Wrong username or password!"
        sys.exit()

def mongo_load(data, args):
    # Make db connection
    client = MongoClient(args.url, int(args.port))
    mongo_db = client[args.database_name]
    collection = mongo_db[args.collection_name]
    mongo_db.authenticate(args.username, args.password)

    collection.insert(data)

    print '%(data_length)i documents inserted into %(col)s collection in the %(db)s database."' % \
        {"data_length": len(data), "col": args.collection_name, "db": args.database_name}

