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
      print("Not able to communicate to with the website. For more information, check the logs.")
      sleep(5)
      exit(code=1)
  

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
      print("Not able to communicate to with the website. For more information, check the logs.")
      sleep(5)
      exit(code=1)
  
  
  def update_system_level_info(self, system_level_info: dict) -> None:
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
  

  def __check_if_log_exists(self, mac_address: str) -> list:
    """
    The function is responsible for checking if the log exists in the database.

    Args:
    - mac_address (str): The mac address of the system.

    Returns:
    - bool: The status of the log.
    """
    
    previous_log_data = self.collection.find_one({"_id": mac_address})
    if previous_log_data:
      previous_log_data_logs = previous_log_data["logs"]
      return previous_log_data_logs
    return []


  def update_logs(self, mac_address: str, logs: list) -> None:
    """
    The function is responsible for updating the logs in the database.

    Args:
    - mac_address (str): The mac address of the system.
    - logs (list): The logs to be updated.

    Returns:
    - None
    """
    
    previous_logs = self.__check_if_log_exists(
      mac_address=mac_address
    )
    
    previous_logs.extend(logs)
    self.collection.update_one(
      filter={"_id": mac_address}, 
      update={"$set": {"logs": previous_logs}}, 
      upsert=True
    )