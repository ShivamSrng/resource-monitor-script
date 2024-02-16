import subprocess
from tqdm import tqdm


class PerformInstallations:
  """
  The PerformInstallations class is responsible for installing the dependancies required for the application.
  """
  
  def __init__(self, installation_list: list) -> list:
    self.installation_list = installation_list
  
  def install(self) -> bool:
    """
    The function is responsible for installing the dependancies required for the application.
    
    Returns:
    - bool: The status of the installation.
    """
    
    return_code = []
    for installation in tqdm(self.installation_list, desc="Installing Dependancies", total=len(self.installation_list)):
      installation_instruction = ["pip", "install", installation]
      result = subprocess.run(installation_instruction, capture_output=True)
      if result.returncode == 0:
        return_code.append(0)
      else:
        return_code.append(1)
        print(f"Failed to install {installation}")
        print(result.stderr.decode("utf-8"))
    if 1 in return_code:
      return False
    else:
      return True