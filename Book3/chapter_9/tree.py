"""
            _2_
           /   \
          7     9
         / \     \
        1   6     8
           / \   / \
          5  10 3   4
"""

class Node:
    def __init__(self, data, left= None, right= None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return repr(self.data)

def create_tree() -> Node:
    two = Node(2)
    seven = Node(7)
    one = Node (1)
    six = Node(6)
    five = Node(5)
    ten = Node(10)

    six.left = five
    six.right = ten

    seven.left = one
    seven.right =  six

    three = Node(3)
    four = Node(4)
    eight = Node(8, three, four)

    nine = Node(9, right=eight)

    two.left = seven
    two.right = nine

    return two

if __name__ == "__main__":
    tree = create_tree()
    print(tree)
