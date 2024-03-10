import re
import psutil
import datetime
import subprocess
from src.logs import Logs


class GetSystemLevelInfo:
  """
  The class is responsible for getting the system level information.
  """
  
  
  def __init__(self, mac_address: str) -> None:
    self.mac_address = mac_address
    self.logger = Logs(mac_address=mac_address)
  
  
  def __get_cpu_info(self) -> dict:
    """
    The function is responsible for getting the CPU information.

    Returns:
    - dict: The CPU information.
    """
    
    try: 
      cpu_related_info = {
        "cpu_count": psutil.cpu_count(),
        "all_cpu_percent": psutil.cpu_percent(interval=0.5, percpu=True)
      }
    except Exception as e:
      self.logger.add_log(
        simplified_error="Not able to get the CPU information",
        complete_error=str(e)
      )
      print("Not able to get the CPU information. For more information, check the logs.")
      exit(code=1)
    return cpu_related_info 
  

  def __get_memory_info(self) -> dict:
    """
    The function is responsible for getting the memory information.

    Returns:
    - dict: The memory information.
    """
    
    try:
      memory_related_info = {
      "memory_total": psutil.virtual_memory().total,
      "memory_available": psutil.virtual_memory().available,
      "memory_percent": psutil.virtual_memory().percent
    }
    except Exception as e:
      self.logger.add_log(
        simplified_error="Not able to get the memory information",
        complete_error=str(e)
      )
      print("Not able to get the memory information. For more information, check the logs.")
      exit(code=1)
    return memory_related_info
  

  def __get_disk_info(self) -> dict:
    """
    The function is responsible for getting the disk information.

    Returns:
    - dict: The disk information.
    """
    
    try:
      disk_related_info = {
        "disk_total": psutil.disk_usage('/').total,
        "disk_used": psutil.disk_usage('/').used,
        "disk_free": psutil.disk_usage('/').free,
        "disk_percent": psutil.disk_usage('/').percent
      }
    except Exception as e:
      self.logger.add_log(
        simplified_error="Not able to get the disk information",
        complete_error=str(e)
      )
      print("Not able to get the disk information. For more information, check the logs.")
      exit(code=1)
    return disk_related_info
  

  def __get_network_info(self) -> dict:
    """
    The function is responsible for getting the network information.

    Returns:
    - dict: The network information.
    """
    
    try:
      network_io_counters = psutil.net_io_counters()
      network_related_info = {
        "bytes_sent": network_io_counters.bytes_sent,
        "bytes_recv": network_io_counters.bytes_recv,
        "packets_sent": network_io_counters.packets_sent,
        "packets_recv": network_io_counters.packets_recv,
        "errin": network_io_counters.errin,
        "errout": network_io_counters.errout,
        "dropin": network_io_counters.dropin,
        "dropout": network_io_counters.dropout
      }
    except Exception as e:
      self.logger.add_log(
        simplified_error="Not able to get the network information",
        complete_error=str(e)
      )
      print("Not able to get the network information. For more information, check the logs.")
      exit(code=1)
    return network_related_info
  

  def __swap_memory_info(self) -> dict:
    """
    The function is responsible for getting the swap memory information.

    Returns:
    - dict: The swap memory information.
    """
    
    try:
      swap_memory = psutil.swap_memory()._asdict()
      swap_memory_related_info = {
        "swap_memory_total": swap_memory["total"],
        "swap_memory_used": swap_memory["used"],
        "swap_memory_free": swap_memory["free"],
        "swap_memory_percent": swap_memory["percent"],
        "swap_memory_sin": swap_memory["sin"],
        "swap_memory_sout": swap_memory["sout"]
      }
    except Exception as e:
      self.logger.add_log(
        simplified_error="Not able to get the swap memory information",
        complete_error=str(e)
      )
      print("Not able to get the swap memory information. For more information, check the logs.")
      exit(code=1)
    return swap_memory_related_info
  
  
  def __get_processes(self) -> list:
    """
    The function is responsible for getting the processes information.

    Returns:
    - list: The processes information.
    """
    try:
      processes_details = subprocess.check_output(['tasklist']).split(b"\r\n")
      process = []
      for task in processes_details:
          match_criteria = re.match(b"(.+?) +(\d+) (.+?) +(\d+) +(\d+.* K).*", task)
          if match_criteria is not None:
              process.append(
                {
                  "image": str(match_criteria.group(1)).replace("b'", '').replace("'", ''),
                  "pid": str(match_criteria.group(2)).replace("b'", '').replace("'", ''),
                  "session_name": str(match_criteria.group(3)).replace("b'", '').replace("'", ''),
                  "session_num": str(match_criteria.group(4)).replace("b'", '').replace("'", ''),
                  "mem_usage": str(match_criteria.group(5)).replace("b'", '').replace("'", '')
                  }
              )
    except Exception as e:
      self.logger.add_log(
        simplified_error="Not able to get the processes information",
        complete_error=str(e)
      )
      print("Not able to get the processes information. For more information, check the logs.")
      exit(code=1)
    return process


  def get_all_info(self) -> dict:
    """
    The function is responsible for getting all the system level information.

    Returns:
    - dict: The system level information.
    """
    
    return {
      "mac_address": self.mac_address,
      "system_level_info": {
        "cpu_info": self.__get_cpu_info(),
        "memory_info": self.__get_memory_info(),
        "disk_info": self.__get_disk_info(),
        "network_info": self.__get_network_info(),
        "swap_memory_info": self.__swap_memory_info(),
        "list_of_processes": self.__get_processes(),
        "last_time_recorded": datetime.datetime.now().strftime("%H:%M:%S")
      }
    }