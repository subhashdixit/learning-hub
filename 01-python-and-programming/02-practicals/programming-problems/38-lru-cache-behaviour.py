"""Implement get/put with capacity2or another positive capacity; get returns None for a missing key."""
from collections import OrderedDict
class Cache:
    def __init__(self,capacity):
        if capacity<=0:raise ValueError('capacity')
        self.capacity=capacity;self.data=OrderedDict()
    def get(self,key):
        if key not in self.data:return None
        self.data.move_to_end(key);return self.data[key]
    def put(self,key,value):
        self.data[key]=value;self.data.move_to_end(key)
        if len(self.data)>self.capacity:self.data.popitem(last=False)
c=Cache(2);c.put('a',1);c.put('b',2);assert c.get('a')==1;c.put('c',3)
assert c.get('b') is None and c.get('c')==3
