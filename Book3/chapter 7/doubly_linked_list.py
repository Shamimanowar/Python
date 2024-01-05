from typing import List


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(data="Head Node")

    def __repr__(self) -> str:
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node.data))
            current_node = current_node.next
        return ",".join(nodes)

    def prepend(self, data):
        node = Node(data=data, next=self.head.next, prev=self.head)

        if self.head.next:
            self.head.next.prev = node
        self.head.next = node
        return node

    def append(self, item):
        current = self.head

        while current.next:
            current = current.next

        node = Node(item, prev=current)
        current.next = node
        return node
    
    def search(self, item):
        current = self.head.next

        while current:
            if current.data == item:
                return current.data
            current = current.next
        return "Not Found"
    
    def remove(self, item):
        current = self.head.next

        if current is None:
            return "List is empty"

        while current:
            if current.data == item:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return current.data
            current = current.next
        return "Item Not Found"

    # The new item will be inserted into the list after the previous data
    def insert(self, item, data=None):
        if data == None: # If no data is provided, then insert the item at the start of the list
            self.prepend(item)
            return self.head.next
        
        current = self.head.next

        while current:
            if current.data == data:
                node = Node(item, next=current.next, prev=current)
                if current.next is not None:
                    current.next.prev = node
                current.next = node
                return node
            current = current.next
        
        return "Data not found"
    