import re

h = '"status":0'
path = re.compile('"status":(\d*)$')
w = path.findall(h)
print(w)