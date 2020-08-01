from singly_linked_list import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.tracker = -1


    def append(self, item):
        self.tracker += 1
        position = self.tracker % self.capacity
        self.storage[position] = item

    def get(self):
        non_null_items = []
        for item in self.storage:
            if item is not None:
                non_null_items.append(item)

        return non_null_items

