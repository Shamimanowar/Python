class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return repr(self.data)
    
    def add_left(self, node) -> None:
        self.left = node
        if node:
            node.parent = self
    
    def add_right(self, node) -> None:
        self.right = node
        if node is not None:
            node.parent = self

def bst_insert(root:TreeNode, node:TreeNode) -> TreeNode:
    last_node = None
    current_node = root

    while current_node is not None:
        last_node = current_node

        if node.data < current_node.data:
            current_node = current_node.left
        elif node.data > current_node.data:
            current_node =  current_node.right
        else:
            print("The data format is not valid")
    
    if last_node is None:
        root = node
    
    if node.data < last_node.data:
        last_node.add_left(node)
    
    if node.data > last_node.data:
        last_node.add_right(node)

    return root

def create_bst():
    root = TreeNode(10)

    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(item)
        root = bst_insert(root=root, node=node)
    
    return root

def inorder_travers(node) -> None:
    if node.left:
        inorder_travers(node.left)

    print(node)
    
    if node.right:
        inorder_travers(node.right)

def bst_search(node: TreeNode, key: int) -> TreeNode:
    
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right
    print("Node not Found")
    return TreeNode(data=None) # Return None

def bst_minimum(node: TreeNode) -> TreeNode:
    while node.left is not None:
        node = node.left
    return node

def bst_transplant(root: TreeNode, target_node: TreeNode, upcoming_node: TreeNode) -> TreeNode:
    if target_node.parent is None:
        root = upcoming_node
    if target_node.parent.left == target_node:
        target_node.parent.add_left(upcoming_node)
    else:
        target_node.parent.add_right(upcoming_node)
    return root

def bst_delete(root: TreeNode, target_node: TreeNode) -> TreeNode:
    if target_node.left is None:
        root = bst_transplant(root, target_node, target_node.right)
    elif target_node.right is None:
        root = bst_transplant(root, target_node, target_node.left)
    else:
        min_node = bst_minimum(target_node.right)
        if min_node.parent != target_node:
            root = bst_transplant(root, min_node, min_node.right)
            min_node.add_right(target_node.right)
        root = bst_transplant(root, target_node, min_node)
        min_node.add_left(target_node.left)


if __name__ == '__main__':
    root = create_bst()
    print(root)