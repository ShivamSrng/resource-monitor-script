from getmac import get_mac_address as gmac
from src.database.database_handler import DatabaseHandler
from src.perform_installations import PerformInstallations
from src.system_info.get_system_level_info import GetSystemLevelInfo


class Engine:
  """
  The Engine class is responsible for executing the application.
  """


  def __init__(self) -> None:
    mac_address = str(gmac()).upper()
    installation_status = self.install_dependencies()
    if not installation_status:
      print("Failed to install dependencies...")
      return
    self.database = DatabaseHandler()
    self.systeminfo = GetSystemLevelInfo(mac_address=mac_address)
  

  def install_dependencies(self) -> bool:
    """
    The function is responsible for installing the dependencies required for the application.

    Returns:
    - bool: The status of the installation.
    """

    dependancies = ["tqdm~=4.66.2", "pymongo~=4.6.1", "certifi~=2024.2.2", "getmac~=0.9.4"]  
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