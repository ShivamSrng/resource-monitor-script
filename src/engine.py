from time import sleep
from src.logs import Logs
from getmac import get_mac_address as gmac
from src.utilities import Utilities
from src.database.database_handler import DatabaseHandler
from src.perform_installations import PerformInstallations
from src.system_info.get_system_level_info import GetSystemLevelInfo


class Engine:
  """
  The Engine class is responsible for executing the application.
  """


  def __init__(self) -> None:
    self.__perform_initial_setup()

  def __perform_initial_setup(self) -> None:
    """
    The function is responsible for performing the initial setup of the application.
    
    Returns:
    - None
    """
    
    
    self.utilities = Utilities()
    self.utilities.program_header(text="DETECTION OF SYSTEM LEVEL INFORMATION")
    self.utilities.paragraph_formatter("Description: The application is responsible for detecting the system level information and communicating with the website to present you with the system level information in a user-friendly manner.Please keep the application running to get the system level information.")
    mac_address = str(gmac()).upper()
    self.logger = Logs(mac_address=mac_address)
    self.utilities.program_sub_header(text="DEPENDENCY INSTALLATION")
    installation_status = self.install_dependencies()
   
    if not installation_status:
      print("Failed to install dependencies...")
      return
    print("Dependencies installed successfully...")
    self.utilities.program_sub_header(text="APPLICATION EXECUTION")
    self.utilities.paragraph_formatter("Please check the website for the system level information and keep the application running in the background. If you want to stop the application, press Ctrl+C.")
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
      try:
        self.database.update_system_level_info(system_level_info)
      except Exception as err:
        self.logger.add_log(
          simplified_error="Not able to insert/update the system level information in the database.",
          complete_error=str(err)
        )
        print("Not able to insert/update the system level information. For more information, check the logs.")
        sleep(5)
        exit(code=1)