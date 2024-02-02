import traceback

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