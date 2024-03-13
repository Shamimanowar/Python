from .tree import create_tree, Node

def pre_order(node: Node) -> None:
    print(node)

    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)
    return

def post_order(node) -> None:
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    
    print(node)
    return

def in_order(node) -> None:
    if node.left:
        in_order(node.left)
        
    print(node)

    if node.right:
        in_order(node.right)
    return
if __name__ == '__main__':
    root = create_tree()
    pre_order(root)
