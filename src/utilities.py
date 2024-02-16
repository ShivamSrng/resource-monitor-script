class Utilities:
  """
  The Utilities class contains the utility methods for the program like formatting the text, etc.
  """
  

  def __init__(self) -> None:
    self.lines = 100
  

  def lines_formatter(self) -> str:
    """
    This method returns a string of lines to be used as a separator.
    
    Returns:
    - str: A string of lines to be used as a separator.
    """
    
    formatted_lines = "-" * self.lines
    return formatted_lines
  

  def center_aligned_formatter(self, text: str) -> str:
    """
    This method returns the text formatted to be center aligned.
    
    Args:
    - text (str): The text to be formatted.
    
    Returns:
    - str: The text formatted to be center aligned.
    """
    
    formatter = int((self.lines - len(text))/2)
    formatted_text = ""
    for _ in range(formatter):
      formatted_text += " "
    formatted_text += text
    for _ in range(formatter):
      formatted_text += " "
    return formatted_text
  

  def program_header(self, text: str) -> None:
    """
    This method prints the header for the program.
    
    Args:
    - text (str): The text to be printed as the header.
    
    Returns:
    - None
    """
    
    print(self.lines_formatter())
    print(self.center_aligned_formatter(text=text))
    print(self.lines_formatter())
    return
  

  def program_sub_header(self, text: str) -> None:
    """
    This method prints the sub-header for the program.
    
    Args:
    - text (str): The text to be printed as the sub-header.
    
    Returns:
    - None
    """
    
    print()
    print(text)
    print(self.lines_formatter())
    return
  

  def paragraph_formatter(self, text: str) -> None:
    """
    This method prints the paragraph for the program, in a way that each line is restricted to at max 100 characters.
    
    Args:
    - text (str): The text to be printed as the paragraph but formatted.
    
    Returns:
    - None
    """

    words = text.split()
    lines = []
    while words:
      line = ""
      while words and len(line + words[0]) <= 100:
        line += words.pop(0) + " "
      lines.append(line)
    for line in lines:
      print(line)
    return