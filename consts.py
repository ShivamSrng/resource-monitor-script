import configparser


class MongoDBConstants:
  def __init__(self) -> None:
    self.config_parser = configparser.ConfigParser()
    self.config_parser.read('config.ini')
    self.config_parser = self.config_parser['MONGODB']
  
  def get_connection_string(self) -> str:
    connection_string = f"mongodb+srv://{self.config_parser['username']}:{self.config_parser['password']}@{self.config_parser['cluster']}.tsvu3gt.mongodb.net/"
    return connection_string
  
  def get_database_name(self) -> str:
    return self.config_parser['database']
  
  def get_collection_name(self) -> str:
    return self.config_parser['collection']