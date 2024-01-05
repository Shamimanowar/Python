class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return repr(self.data)

class SinglyLinkedList:
    
    def __init__(self) -> None:
        self.head = Node()

    def __repr__(self) -> str:
        node = []

        current_node = self.head.next

        while current_node:
            node.append(repr(current_node.data))
            current_node = current_node.next
        
        return ",".join(node)

    def prepend(self, data):
        node = Node(data, next=self.head.next)
        self.head.next = node
        return node

    def append(self, data):
        current_node = self.head.next
        node = Node(data)

        if current_node is None:
            self.head.next = node
            return node

        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node
        return node
        

    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None
    
    def remove(self, data):
        previous = self.head
        current = self.head.next

        if self.head.next is None:
            return

        while current is not None:
            if current.data == data:
                previous.next = current.next
                return current.data
            previous = current
            current = current.next
        
        return "Not Found"


    def insert(self, data, new_item): # The new node should be placed after the data
        node = Node(new_item)
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                node.next = current_node.next
                current_node.next = node
                return node
            
            current_node = current_node.next

        return "{} Not Found".format(data)