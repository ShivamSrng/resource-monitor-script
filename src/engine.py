from src.database.database_handler import DatabaseHandler
from src.system_info.get_system_level_info import GetSystemLevelInfo


class Engine:
  def __init__(self) -> None:
    self.systeminfo = GetSystemLevelInfo()
    self.database = DatabaseHandler()

  def run(self):
    while True:
      system_level_info = self.systeminfo.get_all_info()
      self.database.update_one(system_level_info)
      print("Data Inserted Successfully")   