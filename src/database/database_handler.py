import consts
import pymongo


class DatabaseHandler:
  def __init__(self):
    self.connection_string = consts.MongoDBConstants().get_connection_string()
    self.database_name = consts.MongoDBConstants().get_database_name()
    self.collection_name = consts.MongoDBConstants().get_collection_name()

    self.mongo_client = pymongo.MongoClient(self.connection_string)
    self.db = self.mongo_client[self.database_name]
    self.collection = self.db[self.collection_name]
  
  def insert_one(self, data):
    self.collection.insert_one(data)
  
  def update_one(self, system_level_info: dict):
    self.collection.update_one({"_id": system_level_info["mac_address"]}, {"$set": system_level_info["system_level_info"]}, upsert=True)