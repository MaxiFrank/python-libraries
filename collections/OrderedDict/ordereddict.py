from collections import OrderedDict

"""
class collections.OrderedDict([items])
Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.
"""

d = OrderedDict.fromkeys('abcde')
# print(d)
# d.move_to_end('b')

# print(''.join(d))
print(d)
pair = d.popitem()
print(pair)
print(d)
