
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.length = 0 if self.value is None else 1

    
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


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        contained = False
        if target == self.value:
            return True

        if target < self.value:
            if self.left:
                if target == self.left.value:
                    contained = True
                else:
                    self.left.contains(target)
            else:
                return contained

        if target > self.value:
            if self.right:
                if target == self.right.value:
                    contained = True
                else:
                    self.right.contains(target)
            else:
                return False
        return contained
