import datetime
import traceback

from bson import ObjectId

import constants

class ApiHelper:
    def __init__(self, mongo_util_obj):
        self.mongo_util_obj = mongo_util_obj

    def get_all_products(self, collection_name, limit, offset, min_price = None, max_price = None):
        result = {"data": [], "page": {"limit": limit, "nextOffset": None, "prevOffset": None, "total": 0}}
        try:
            filter_query = {}
            if min_price or max_price:
                if min_price:
                    filter_query["$gte"] = min_price
                if max_price:
                    filter_query["$lte"] = max_price
                filter_query = {"price": filter_query}

            pipeline = [
                            {"$match": filter_query},
                            {"$group": {"_id": None, "total_records": {"$sum": 1}, "products": {"$push": "$$ROOT"}}},
                            {"$project": {"_id": 0, "total_records": 1, "products": {"$slice": ["$products", offset, limit]}}},
                       ]
            mongo_result = self.mongo_util_obj.aggregate_pipeline(collection_name, pipeline)
            if mongo_result:
                metadata = {
                                "limit": limit,
                                "nextOffset": offset + limit if offset + limit < mongo_result[0]["total_records"] else None,
                                "prevOffset": offset - limit if offset - limit >= 0 else None,
                                "total": mongo_result[0]["total_records"],
                            }
                products = [{"id": str(product["_id"]), "name": product["name"], "price": product["price"], "quantity": product["avail_qty"]} for product in mongo_result[0]["products"]]
                result = {"data": products, "page": metadata}
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return result

    def create_order(self, collection_name, order_data):
        order_data["createdOn"] = datetime.datetime.now()
        order_id = self.mongo_util_obj.insert_one_document(collection_name, order_data, confirm=True)
        if order_id:
            reduced_order_qty = []
            for each_item in order_data["items"]:
                query_dict = {"query": [
                                            {"_id": ObjectId(each_item["productId"])},
                                            {"$inc": {"avail_qty": -each_item["boughtQuantity"]}}
                                        ]
                            }
                reduced_order_qty.append(query_dict)
            self.mongo_util_obj.bulk_updates(constants.product_collection, reduced_order_qty)
        return order_id