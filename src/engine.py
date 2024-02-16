from src.database.database_handler import DatabaseHandler
from src.perform_installations import PerformInstallations
from src.system_info.get_system_level_info import GetSystemLevelInfo


class Engine:
  """
  The Engine class is responsible for executing the application.
  """

  def __init__(self) -> None:
    installation_status = self.install_dependencies()
    if not installation_status:
      print("Failed to install dependencies...")
      return
    self.database = DatabaseHandler()
    self.systeminfo = GetSystemLevelInfo()
  
  def install_dependencies(self) -> bool:
    """
    The function is responsible for installing the dependencies required for the application.

    Returns:
    - bool: The status of the installation.
    """

    dependancies = []
    with open("requirements.txt", "r") as file:
      dependancies = file.readlines()
    
    installation_status = PerformInstallations(dependancies).install()
    if installation_status:
      return True
    return False

  def run(self) -> None:
    """
    The function is responsible for running the application and serializing the execution of the system level info and database handler.
    """

    print("Communicating with the website...")
    while True:
      system_level_info = self.systeminfo.get_all_info()
      self.database.update_one(system_level_info)
