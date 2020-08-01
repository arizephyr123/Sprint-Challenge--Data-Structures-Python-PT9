class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        elements = []

        element = self.head
        while element is not None:
            elements.append(element.get_value())
            element = element.get_next()

        return str(elements)

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        if node is None:
            return None
        if node.get_next() is None:
            self.head = node
            return
        if node.get_next() is not None:
            print('while', node.value, 'next ->', node.next_node.value, "head ->", self.head.value)
            self.reverse_list(node.get_next())
            old_after = node.get_next()
            old_after.set_next(node)
            node.set_next(None)
            
        

ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
ll.add_to_head(4)
ll.add_to_head(5)
print(ll)
print(ll.head.value, ' == 5?')
ll.reverse_list(ll.head)
print(ll)
print(ll.head.value, ' == 1?')
print(ll.head.get_next().value, ' == 2?')
print(ll.head.get_next().get_next().value,' == 3?')
