import pymongo

# Basic options for pymongo
# http://api.mongodb.org/python/current/tutorial.html

# Mongo/Python/Flask application tutorial
# https://docs.mongodb.org/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/
client = pymongo.MongoClient(host='192.168.1.33', port=27017)
print("Done")

