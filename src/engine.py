from src.database.database_handler import DatabaseHandler
from src.system_info.get_system_level_info import GetSystemLevelInfo


class Engine:
  """
  The Engine class is responsible for executing the application.
  """

  def __init__(self) -> None:
    self.database = DatabaseHandler()
    print("Established connection with the database...")
    self.systeminfo = GetSystemLevelInfo()

  def run(self) -> None:
    """
    The function is responsible for running the application and serializing the execution of the system level info and database handler.
    """

    print("Communicating with the database...")
    while True:
      system_level_info = self.systeminfo.get_all_info()
      self.database.update_one(system_level_info)