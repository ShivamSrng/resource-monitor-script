import consts
import pymongo
import certifi
from time import sleep


class DatabaseHandler:
  """
  The class is responsible for handling the database operations.
  """
  
  def __init__(self) -> None:
    self.mongo_client = self.__establish_connection()

    try:
      self.db = self.mongo_client[self.database_name]
      self.collection = self.db[self.collection_name]
    except Exception as err:
      print(err)
      sleep(10)
      self.mongo_client.close()
  
  def __establish_connection(self) -> pymongo.MongoClient:
    """
    The function is responsible for establishing a connection with the MongoDB database.

    Returns:
    - pymongo.MongoClient: The MongoDB client.
    """
    self.connection_string = consts.MongoDBConstants().get_connection_string()
    self.database_name = consts.MongoDBConstants().get_database_name()
    self.collection_name = consts.MongoDBConstants().get_collection_name()

    try:
      self.mongo_client = pymongo.MongoClient(
        self.connection_string, 
        tlsCAFile=certifi.where()
      )
      client_info = self.mongo_client.server_info()
      return self.mongo_client
    
    except Exception as err:
      print("Not able to communicate: ", err)
      return False

  
  def update_one(self, system_level_info: dict) -> None:
    """
    The function is responsible for updating the system level information in the database. If the system level information is not present, it will insert the system level information, else it will update the system level information.

    Args:
    - system_level_info (dict): The system level information.

    Returns:
    - None
    """
    
    self.collection.update_one(
      filter={"_id": system_level_info["mac_address"]}, 
      update={"$set": system_level_info["system_level_info"]}, 
      upsert=True
    )