import constants

from fastapi import FastAPI, Query

from models import Order
from api_helper import ApiHelper
from mongo_utils import MongoUtils

mongo_obj = MongoUtils(constants.host, constants.database)
app = FastAPI()

@app.get("/products")
async def get_products(
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        min_price: float = Query(None, ge=0, description="Minimum price filter"),
        max_price: float = Query(None, ge=0, description="Maximum price filter")
):
    api_helper_obj = ApiHelper(mongo_obj)
    result = api_helper_obj.get_all_products(constants.product_collection, limit, offset, min_price, max_price)
    return result

@app.post("/make_order")
async def create_order(order_data: Order):
    api_helper_obj = ApiHelper(mongo_obj)
    order_id = api_helper_obj.create_order(constants.order_collection, order_data.dict())
    result_dict = {"message": "Order created successfully", "order_id": order_id}
    return result_dict
