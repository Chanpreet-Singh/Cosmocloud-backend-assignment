from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    productId: str
    boughtQuantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str

class Order(BaseModel):
    items: List[Product]
    totalAmount: float
    userAddress: UserAddress