# deque

class collections.deque([iterable[, maxlen]])

Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.

Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end.

Pop on either side is O(1)