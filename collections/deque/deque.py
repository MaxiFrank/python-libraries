from collections import deque

print("deque is", deque([1, 2, 3]))


# append(x): Add an element on the right side of the deque
def append(x):
    d = deque([1, 2, 3])
    d.append(x)
    print(append.__name__, x, "is", d)


# appendleft(x): Add an element on the left side of the deque
def appendleft(x):
    d = deque([1, 2, 3])
    d.appendleft(x)
    print(appendleft.__name__, x, "is", d)


# pop(): Remove an element from the right side of the deque
def pop():
    d = deque([1, 2, 3])
    d.pop()
    print(pop.__name__, "is", d)


# popleft(): Remove an element from the left side of the deque
def popleft():
    d = deque([1, 2, 3])
    d.popleft()
    print(popleft.__name__, "is", d)


# extend(iterable): Add multiple elements to the right side of the deque
def extend(iterable):
    d = deque([1, 2, 3])
    d.extend(iterable)
    print(extend.__name__, iterable, "is", d)


# extendleft(iterable): Add multiple elements to the left side of the deque
def extendleft(iterable):
    d = deque([1, 2, 3])
    d.extendleft(iterable)
    print(extendleft.__name__, iterable, "is", d)


# rotate(): Rotate the deque
def rotate(n):
    d = deque([1, 2, 3])
    d.rotate(n)
    print(rotate.__name__, n, "is", d)


# clear(): Remove all elements from the deque
def clear():
    d = deque([1, 2, 3])
    d.clear()
    print(clear.__name__, "is", d)


# count(x): Count the number of occurrences of an element in the deque
def count(n):
    d = deque([1, 2, 3])
    print(count.__name__, n, "is", d.count(n))


# index(x): Return the index of the first occurrence of an element in the deque
def index(n):
    d = deque([1, 2, 3])
    print(index.__name__, n, "is", d.index(n))


# insert(i, x): Insert an element at a specific position in the deque
def insert(i, x):
    d = deque([1, 2, 3])
    d.insert(i, x)
    print(insert.__name__, x, "at index", i, "is", d)


# remove(x): Remove the first occurrence of an element from the deque
def remove(n):
    d = deque([1, 2, 3])
    d.remove(n)
    print(remove.__name__, "first occurance of", n, "is", d)


# reverse(): Reverse the order of the elements in the deque
def reverse():
    d = deque([1, 2, 3])
    d.reverse()
    print(reverse.__name__, "is", d)


if __name__ == "__main__":
    append(4)
    appendleft(0)
    pop()
    popleft()
    extend([5, 6, 7])
    extendleft([8, 9, 10])
    rotate(1)
    clear()
    count(2)
    index(1)
    insert(4, 3)
    remove(2)
    reverse()
