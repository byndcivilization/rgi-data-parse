#!/usr/bin/python
"""Loads parsed data into mongodb"""

from pymongo import MongoClient

def mongo_load(data, db_name, collection_name, username, password, environment):
    """Parses and loads RGI questions from excel into MongoDB"""
	# Make db connection
    if environment == 'local':
        mongo_url = 'mongodb://localhost'
    elif environment == 'remote':
        mongo_url = 'mongodb://' + username + ':' + password + '@candidate.32.mongolayer.com:10582/rgi2015_dev'
	# client = MongoClient('localhost',27017)
    client = MongoClient(mongo_url)
    mongo_db = client[db_name]
    collection = mongo_db[collection_name]

    try:
        mongo_db.authenticate(username, password)
        print "Authenticated Mongo connection."

        # collection.insert(data)

        # print str(len(data)) + " documents inserted into " + collection_name + \
        # " collection in the "+ db_name + " database."

    except:
        print "Wrong username or password!"


#     if (env === 'local') {
#         mongoose.connect(config.db);
#     } else {
#         mongoose.connect('mongodb://' + user + ':' + pass + config.db);
#     }

#         local: {
#     db: 'mongodb://localhost/rgi2015_dev',
#         rootPath: rootPath,
#         port: process.env.PORT || 3030
#     },
#     development: {
#         db: '@candidate.32.mongolayer.com:10582/rgi2015_dev',
#         rootPath: rootPath,
#         port: process.env.PORT || 80
#     },
#     production: {
#         db: '@candidate.32.mongolayer.com:10582/rgi2015_production',
#         rootPath: rootPath,
#         port: process.env.PORT || 80
#     }
# };