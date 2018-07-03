import re

# h = '"status":0'
# path = re.compile('"status":(\d*)$')
# w = path.findall(h)
# print(w)

h = 'UTC-09:00'
path = re.compile('^UTC([+|-]\d\d):00$')
w = path.findall(h)
print(w)