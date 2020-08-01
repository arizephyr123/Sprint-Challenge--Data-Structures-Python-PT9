from singly_linked_list import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = LinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else: 
            self.storage.add_to_tail(item)
            self.storage.remove_head()

    def get(self):
        non_null_items = []

        if self.storage.length == 0:
            pass

        else:
            curr_node = self.storage.head
            i = 1
            while i < self.storage.length +1:
                non_null_items.append(curr_node.value)
                curr_node = curr_node.get_next()
                i += 1
        return non_null_items




buffer = RingBuffer(3)
# print('buffer', buffer)
buffer.storage.print_list()
print('get', buffer.get()   , "should return []")

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.storage.print_list()
print(buffer.get()   , "should return ['a', 'b', 'c']")

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')
# buffer.storage.print_list()

print(buffer.get()   , "should return ['d', 'b', 'c']")

buffer.append('e')
buffer.storage.print_list()
buffer.append('f')
buffer.storage.print_list()

print(buffer.get(),    "should return ['d', 'e', 'f']")