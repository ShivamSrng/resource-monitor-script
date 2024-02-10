import consts
import pymongo


class DatabaseHandler:
  """
  The class is responsible for handling the database operations.
  """
  
  def __init__(self) -> None:
    self.connection_string = consts.MongoDBConstants().get_connection_string()
    self.database_name = consts.MongoDBConstants().get_database_name()
    self.collection_name = consts.MongoDBConstants().get_collection_name()

    self.mongo_client = pymongo.MongoClient(self.connection_string)
    self.db = self.mongo_client[self.database_name]
    self.collection = self.db[self.collection_name]

  
  def update_one(self, system_level_info: dict) -> None:
    """
    The function is responsible for updating the system level information in the database. If the system level information is not present, it will insert the system level information, else it will update the system level information.

    Args:
    - system_level_info (dict): The system level information.

    Returns:
    - None
    """
    
    self.collection.update_one({"_id": system_level_info["mac_address"]}, {"$set": system_level_info["system_level_info"]}, upsert=True)