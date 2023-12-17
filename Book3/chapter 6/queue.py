class Queue:
    
    def __init__(self):
        self.items = []
        self.head, self.tail = 0, 0

    def _is_empty(self):
        if self.items == []:
            return True
        return False

    def enqueue(self, item):
        self.items.append(item)
        self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            print("No item left to dequeue")
            return
        if not self._is_empty():
            item = self.items[self.head]
            self.head += 1
            return item
        print("Queue is empty!")
        return
    
    @property
    def size(self):
        return len(self.items)
    

class CircularQueue:
    
    def __init__(self, max_size=100):
        self.items = ["*"] * max_size
        self.head, self.tail, self.size = 0, 0, 0
        self.max_size = max_size

    def enqueue(self, item):
        if not self.is_full():
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            return

        print("Queue is full!")

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.max_size
    
    





if __name__ == "__main__":
    # q = Queue()
    # cq = CircularQueue(5)
    # li = list(range(5))

    # for i in li:
    #     q.enqueue(i)

    # for i in range(4):
    #     cq.enqueue(i)
    
    # while not cq.is_empty():
    #     print(f"head={cq.head} tail={cq.tail} items={cq.items}", end=' ')
    #     item = cq.dequeue()
    #     print(f"item={item}")
        
    # cq.dequeue()
    # cq.dequeue()
    # cq.enqueue(10)

    # print(f"Final results head={cq.head} tail={cq.tail} items={cq.items}")

    cq = CircularQueue(3)

    cq.enqueue("Tahmid")
    cq.enqueue("Rafi")
    cq.enqueue("Tamim")
    cq.enqueue("Subeen")

    while not cq.is_empty():
        person = cq.dequeue()
        print(person)

    cq.enqueue("Subeen")
    # q.enqueue("Subeen")
    
    print(cq.items)
    print(f"head={cq.head} and tail={cq.tail}")