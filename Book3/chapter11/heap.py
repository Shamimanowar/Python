# Heap is a complete binary tree
from typing import List

def left(i: int) -> int:
    return i*2
def right(i: int) -> int:
    return i*2 + 1
def parent(i: int) -> int:
    return i//2


def max_heapify(heap: List[int], heap_size: int, i:int) -> None:
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    
    if r <= heap_size and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        if largest * 2 > heap_size: #If largest is big, left, right > heap_size
            return
        max_heapify(heap, heap_size, largest)

def build_max_heap(heap):
    heap_size = len(heap) - 1
    print(f"{heap_size:_^40}")

    for i in range(heap_size//2, 0, -1):
        max_heapify(heap, heap_size, i)

    return heap


def heap_sort(heap):
    build_max_heap(heap=heap)
    heap_size = len(heap) - 1

    for i in range(heap_size, 1, -1):
        heap[i], heap[1] = heap[1], heap[i]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)
        print(f"{i = } and {heap = }")


def get_maximum(heap):
    return heap[1]

def extract_max(heap, heap_size):
    max_heap = heap[1]
    heap[1] = heap[heap_size]
    heap_size -= 1
    max_heapify(heap, heap_size, 1)
    return max_heap

def insert_node(heap, heap_size, node_value):
    heap = build_max_heap(heap)
    heap_size += 1
    i = heap_size

    heap[i] = node_value

    while i> 1 and heap[i] > heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)
    return heap_size

def increase_key(heap, i, new_value):
    heap[i] = new_value

    while i > 1 and heap[i] > heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)