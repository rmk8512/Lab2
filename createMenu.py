def createMenu(optionList):
    """
    precondition: None
    postconditions: None
    description: retrieves the string of values
    """  
  tmp = ' '; ct = 0
  for opt in optionList:
    tmp += str(ct) + '.' + opt + '\n'
    ct += 1
  return tmp
