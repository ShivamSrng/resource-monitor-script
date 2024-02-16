import psutil
import datetime
from getmac import get_mac_address as gmac
from src.utilities import Utilities


class GetSystemLevelInfo:
  
  def __init__(self) -> None:
    self.utilities = Utilities()

  def __get_cpu_info(self) -> dict:
    """
    The function is responsible for getting the CPU information.

    Returns:
    - dict: The CPU information.
    """
    
    return {
      "cpu_count": psutil.cpu_count(),
      "all_cpu_percent": psutil.cpu_percent(interval=0.5, percpu=True)
    }
  

  def __get_memory_info(self) -> dict:
    """
    The function is responsible for getting the memory information.

    Returns:
    - dict: The memory information.
    """
    
    return {
      "memory_total": psutil.virtual_memory().total,
      "memory_available": psutil.virtual_memory().available,
      "memory_percent": psutil.virtual_memory().percent
    }
  

  def __get_disk_info(self) -> dict:
    """
    The function is responsible for getting the disk information.

    Returns:
    - dict: The disk information.
    """
    
    return {
      "disk_total": psutil.disk_usage('/').total,
      "disk_used": psutil.disk_usage('/').used,
      "disk_free": psutil.disk_usage('/').free,
      "disk_percent": psutil.disk_usage('/').percent
    }
  

  def __get_network_info(self) -> dict:
    """
    The function is responsible for getting the network information.

    Returns:
    - dict: The network information.
    """
    
    return {
      "network_io_counters": psutil.net_io_counters()
    }
  

  def __swap_memory_info(self) -> dict:
    """
    The function is responsible for getting the swap memory information.

    Returns:
    - dict: The swap memory information.
    """
    
    return {
      "swap_memory": psutil.swap_memory()._asdict()
    }
  

  def get_all_info(self) -> dict:
    """
    The function is responsible for getting all the system level information.

    Returns:
    - dict: The system level information.
    """
    
    return {
      "mac_address": str(gmac()).upper(),
      "system_level_info": {
        "cpu_info": self.__get_cpu_info(),
        "memory_info": self.__get_memory_info(),
        "disk_info": self.__get_disk_info(),
        "network_info": self.__get_network_info(),
        "swap_memory_info": self.__swap_memory_info(),
        "last_time_recorded": datetime.datetime.now().strftime("%H:%M:%S")
      }
    }
