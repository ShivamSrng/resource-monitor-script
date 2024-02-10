class Utilities:
  
  def __init__(self) -> None:
    self.lines = 50
  
  def lines_formatter(self) -> str:
    formatted_lines = "-" * self.lines
    return formatted_lines
  
  def center_aligned_formatter(self, text: str) -> str:
    formatter = int((self.lines - len(text))/2)
    formatted_text = ""
    for _ in range(formatter):
      formatted_text += " "
    formatted_text += text
    for _ in range(formatter):
      formatted_text += " "
    return formatted_text
  
  def program_header(self, text: str) -> None:
    print(self.lines_formatter())
    print(self.center_aligned_formatter(text=text))
    print(self.lines_formatter())
    return
  
  def program_sub_header(self, text: str) -> None:
    print()
    print(text)
    print(self.lines_formatter())
    return
