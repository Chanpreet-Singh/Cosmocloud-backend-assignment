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

    def insert_one_document(self, collection_name, data_document, confirm = False):
        inserted_document_id = None
        try:
            collection = self.database[collection_name]
            result = collection.insert_one(data_document)
            if confirm:
                query = {"_id": result.inserted_id}
                inserted_data = self.find_one_document(collection_name, query)
                if inserted_data:
                    inserted_document_id = str(inserted_data["_id"])
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return inserted_document_id

    def find_one_document(self, collection_name, query_dict={}):
        data_dict = {}
        try:
            collection = self.database[collection_name]
            data_dict = collection.find_one(query_dict)
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return data_dict

    def bulk_updates(self, collection_name, list_query_dict):
        try:
            collection = self.database[collection_name]
            for each_query_dict in list_query_dict:
                collection.update_one(each_query_dict["query"][0], each_query_dict["query"][1])
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
