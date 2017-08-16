#!/usr/bin/env python3
# database.py
"""
Provides a layer by which the app accesses the data in the database.
"""

import pymongo
from datetime import datetime
from bson.objectid import ObjectId
from argon2 import PasswordHasher
import bcrypt

pw = PasswordHasher()

class Receipt():
    def __init__(self, goods: {"Good": int}, location: "Location", time: datetime, user: "User"):
        self.goods = goods
        self.location = location
        self.time = time
        self.user = user

class Good():
    def __init__(self, item: "Item", price, abbreviation: str, location: "Location"):
        self.item = item
        self.price = price
        self.abbreviation = abbreviation
        self.location = location

class Item():
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

class User():
    def __init__(self, name: dict, username: str, email: str, phash: str, isStaff: bool, validated: bool):
        self.name = name
        self.username = username
        self.email = email
        self.isStaff = isStaff
        self.validated = validated
        self.tokens = ""

class Preceipt():
    def __init__(self, user:"User", text:str):
        self.user = user
        self.text = text

class Location():
    def __init__(self, location):
        self.location = location

db = pymongo.MongoClient().ledgr
collections = {Receipt: db.receipts, Good: db.goods, Item: db.items,
               User: db.users, Location: db.locations, Preceipt: db.preceipt}


# Create indexes for collections
db.items.create_index([("name", pymongo.ASCENDING), ("brand", pymongo.ASCENDING)], unique=True)
db.goods.create_index([("item", pymongo.ASCENDING), ("location", pymongo.ASCENDING)], unique=True)
db.users.create_index("username")
db.users.create_index("email")
db.users.create_index("tokens")
db.locations.create_index("location")
db.preceipt.create_index("text")

def insert(objects) -> [ObjectId]:
    """
    Takes a list of objects that are of the same type, and inserts them.
    Returns the ObjectId of each in a list in a corresponding order.
    """
    inserted_ids = []
    collection = collections[type(objects[0])]
    for object in objects:
        inserted_ids.append(collection.insert_one(object.__dict__))
    return inserted_ids

"""
def insert_receipt(receipts: [Receipt]) -> [ObjectId]:
    inserted_ids = []
    for receipt in receipts:
        inserted_ids.append( db.receipts.insert_one(receipt.__dict__) )
    return inserted_ids

def insert_good(goods: [Good]) -> [ObjectId]:
    inserted_ids = []
    for good in goods:
        inserted_ids.append( db.goods.insert_one(good.__dict__) )
    return inserted_ids

def insert_item(items: [Item]) -> [ObjectId]:
    inserted_ids = []
    for item in items:
        inserted_ids.append( db.items.insert_one(item.__dict__) )
    return inserted_ids

def insert_user(users: [User]) -> [ObjectId]:
    inserted_ids = []
    for user in users:
        inserted_ids.append( db.users.insert_one(user.__dict__) )
    return inserted_ids

def insert_location(locations: [Location]) -> [ObjectId]:
    inserted_ids = []
    for location in locations:
        inserted_ids.append( db.locations.insert_one(user.__dict__) )
    return inserted_ids
"""


def find(obj_type, **search_terms) -> ["Object"]:
    """
    Takes the type of an object, and the search terms.

    eg:
    import database
    database.find(database.Item, name="Sausage")

    Will return a list of objects meeting that criteria. Empty if none.
    """
    collection = collections[type(objects[0])]
    results = []
    for object in collection.find(search_terms):
        result = obj_type.__new__(obj_type)
        result.__dict__ = object
        results.append(result)
    return results

"""
def find_receipt(**search_terms) -> [Receipt]:
    results = []
    for receipt in db.receipts.find(search_terms):
        del receipt["_id"]
        result = Receipt.__new__(Receipt)
        result.__dict__ = receipt
        results.append(result)
    return results

def find_good(**search_terms) -> [Good]:
    results = []
    for good in db.goods.find(search_terms):
        del good["_id"]
        result = Good.__new__(Good)
        result.__dict__ = good
        results.append(result)
    return results

def find_item(**search_terms) -> [Item]:
    results = []
    for item in db.items.find(search_terms):
        del item["_id"]
        result = Item.__new__(Item)
        result.__dict__ = item
        results.append(result)
    return results

def find_user(**search_terms) -> [User]:
    results = []
    for user in db.users.find(search_terms):
        del user["_id"]
        result = User.__new__(User)
        result.__dict__ = user
        results.append(result)
    return results

def find_location(**search_terms) -> [Location]:
    results = []
    for location in db.locations.find(search_terms):
        del location["_id"]
        result = Location.__new__(User)
        result.__dict__ = location
        results.append(result)
    return results
"""
