from collections import defaultdict

"""
Return a new dictionary-like object
The factory_default, in the cases below, list and int, are default values that are assigned to the key 'missing_key'

"""


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
print(d)

for k, v in s:
    d[k].append(v)

print(d)

"""
>>> defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
"""

d = defaultdict(int)

s = [1, 1, 2, 3, 4]

for n in s:
    d[n] += 1

print(d["missing_key"])
">>> return 0"