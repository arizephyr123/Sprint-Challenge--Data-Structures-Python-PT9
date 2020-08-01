
class BinarySearchTree:
    def __init__(self, value=''):
        self.value = value
        self.left = None
        self.right = None
        self.length = 1 if self.value is not '' else 0

    def create(arr):
        root = None
        for item in arr:
            root = insert(root, item)
        return root

    def search(root, name, depth=1):
        if not root:
            return 
        elif root.value == name:
            return root.value
        elif name < root.value:
            return search(root.left, name, depth + 1)
        else:
            return search(root.right, name, depth + 1)


    def insert(self, value):
        self.length += 1
        # if value <= self.value:
        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # def search(self, val, depth=1):
    #     curr_node = self
    #     if not self:
    #         pass 
    #     elif self.value == val:
    #         # depth could be returned to see how far item is from root
    #         # return curr_node.value, depth
    #         return curr_node.value
    #     elif val < self.value and self.left:
    #         curr_node = self.left
    #         return curr_node.search(val, depth + 1)
    #     elif val > self.value and self.right:
    #         curr_node = self.right
    #         return curr_node.search(val, depth + 1)
    #     else: 
    #         pass

    
            




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False


