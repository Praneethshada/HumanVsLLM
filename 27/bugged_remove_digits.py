
import re
def remove(list):
  pattern = '[1-9]'
  list = [re.sub(pattern, '', i) for i in list]
  return list
