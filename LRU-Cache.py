class LRUCache:

    def __init__(self, capacity: int):
        # use deque to represent most recently used keys
        # use map to allow getting and putting
        self.memory = []
        self.storage = {}
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.storage:
            # append key:val to back of list
            idx = 0
            for i in range(len(self.memory)):
                if self.memory[i] == key:
                    idx = i
            self.memory.pop(idx)
            self.memory.append(key)
            return self.storage[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage[key] = value
            idx = 0
            for i in range(len(self.memory)):
                if self.memory[i] == key:
                    idx = i
            self.memory.pop(idx)
            self.memory.append(key)
        else:
            if self.size + 1 > self.capacity:
                # evict least recently used node
                # front of list represents least recently used
                # back of list represents most recently used
                remove = self.memory.pop(0)
                del self.storage[remove]
            self.size += 1
            self.storage[key] = value
            self.memory.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)