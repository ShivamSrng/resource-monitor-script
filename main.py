from time import sleep
from src.utilities import Utilities
from src.engine import Engine


if __name__ == "__main__":
  """
  The main function of the program and is the entry point of the program. It creates an instance of the Engine class and runs it. It fetches the system level information and displays it to the user on the website.
  """
  
  try:
    Engine().run()
  except KeyboardInterrupt as e:
    print()
    print(Utilities().lines_formatter())
    print("Exiting the application...")
    print(Utilities().lines_formatter())
    sleep(5)
    exit(code=0)