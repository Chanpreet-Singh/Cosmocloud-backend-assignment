import traceback

from pymongo import MongoClient

class MongoUtils:
    def __init__(self, host, database):
        self.client = MongoClient("mongodb://{0}:27017/".format(host))
        self.database = self.client[database]

    def aggregate_pipeline(self, collection_name, pipeline):
        try:
            collection = self.database[collection_name]
            result = list(collection.aggregate(pipeline))
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return result