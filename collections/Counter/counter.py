from collections import Counter

"""class collections.Counter([iterable-or-mapping])
A Counter is a dict subclass for counting hashable objects. 
It is a collection where elements are stored as dictionary keys and 
their counts are stored as dictionary values. 
"""

c = Counter("gallahad")
print(c)

c = Counter(cats=4, dogs=8)
print(c)

print(c.most_common(1))
print(c.most_common(2))
print(c.most_common(3))
print(c.most_common(4))