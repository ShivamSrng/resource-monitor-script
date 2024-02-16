from datetime import datetime
from src.database.database_handler import DatabaseHandler

class Logs:
  """
  The class is responsible for logging the system level information.
  """


  def __init__(self, mac_address: str) -> None:
    self.mac_address = mac_address
    self.log_format = {
      "_id": mac_address,
      "logs": []
    }
  

  def add_log(self, simplified_error: str, complete_error: str) -> None:
    """
    The function is responsible for adding the logs to the log format.

    Args:
    - simplified_error (str): The simplified error.
    - complete_error (str): The complete error.

    Returns:
    - None
    """

    self.log_format["logs"].append({
      "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
      "simplified_error": simplified_error,
      "complete_error": complete_error
    })

    DatabaseHandler().update_logs(
      mac_address=self.mac_address, 
      logs=self.log_format["logs"]
    )
