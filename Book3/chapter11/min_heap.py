"""
min-heap implementation
"""
from typing import List, Optional

def left(i:int) -> int:
    return i * 2

def right(i:int) -> int:
    return i * 2 + 1

def parent(i:int) -> int:
    return i // 2

def min_heapify(heap: List[int], heap_size: int, i: int) -> List[int]:
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] < heap[i]:
        smallest = l
    else:
        smallest = r