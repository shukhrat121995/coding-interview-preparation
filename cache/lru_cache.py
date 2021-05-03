"""
The slow approach implementation is just simple but it is not efficient at all (and it is ugly).
The fast approach implementation is much better using OrderedDict (so that you have O(1) access time).
OrderedDict has .move_to_end() and .popitem(last=False) #last=True if you want to pop the last element,
last=False if you want to pop the first element which make things way too easy.

Why do I do this? Well, if I were interviewed, I would tell the interviewer the first approach too and then
introduce the second approach for faster time. By doing so, the interviewer knows my thinking process,
my knowledge on Python data structures and my communication skills.

Things to keep in mind:
Putting

Whenever you are putting a key-value pair in, you have to check whether the key already exists.
If it exists, you get that key-value pair, update the value and put that pair at the the end of the cache.
If the key does not exist, you check whether the cache size is already at limit.
If the cache size is at limit, pop the key-value pair at the beginning of the cache and push the new key-value
pair at the end of the cache.
If the cache is still under size limit, simply push the new key-value pair at the end of the cache.
Getting

Whenever you are getting the value of the key, check whether the key exists in the cache.
If it exists, put that key-value pair at the end of the cache and return the value.
If it does not exist, return -1.
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()  # OrderedDict is fast because it uses Doubly Linked List internally.

    def get(self, key: int) -> int:
        if key in self.cache:
            # OrderedDict was faster than using deque was the method move_to_end()
            # in OrderedDict is in O(1) time complexity (it uses a dictionary to record the location of each element)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.size:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key)
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
