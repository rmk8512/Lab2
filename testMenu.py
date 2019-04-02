##def createMenu(optionList):
##  tmp = ''; ct = 0
##  for opt in optionList:
##    tmp += str(ct) + '.' + opt + '\n'
##    ct += 1
##  return tmp
##

optionList = ["start","stop","restart","quit"]
print(createMenu(optionList))


optionList = ["begin","request","pay","quit"]
print(createMenu(optionList))


optionList = ["withdrawal","deposit","show","quit"]
print(createMenu(optionList))

