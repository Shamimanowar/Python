from typing import Optional

class Recursion:
    def __init__(self) -> None:
        pass
    
    def factorial(self, n: int) -> int:
        if n in [0, 1]:
            return 1
        
        return n * self.factorial(n -1)
    
    def binary_search_recursive(self, left: int, right: int, L: list, n: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        
        if L[mid] == n:
            return mid

        if n > L[mid]:
            left = mid + 1
            return self.binary_search_recursive(left, right, L, n)
        else:
            right = mid - 1
            return self.binary_search_recursive(left, right, L, n)
        
    def binary_search(self, L, left, right, x):
        if left > right: 
            return -1
        mid = (left+right) // 2

        if L[mid] == x:
            return mid
        if L[mid] < x:
            return self.binary_search(L, mid+1, right, x)
        else:
            return self.binary_search(L, left, mid-1, x)

# a = Recursion()
# test = a.binary_search_recursive(left, right, L, n) L = [1, 3, 5, 6, 7, 8, 12]   left, right = 0, len(L) -1
    
def print_number(n: int) -> None:
    if n == 0:
        return
    
    # print(n)
    print_number(n-1)
    print(n)


def binary_search(n: int, L: list = []) -> int:
    if not L:
        L = [1, 4, 5, 6, 10, 13, 15, 17, 18, 21, 29, 32, 34, 35, 37, 40, 46, 49, 53, 57, 100, 159, 205, 305, 400, 406, 506]
    
    while True:
        length = len(L)
        mid = L[length//2]

        if mid == n:
            return mid
        if mid < n:
            L = L[length//2 + 1:]
        if mid > n:
            L = L[:length//2]
        if not L:
            return -1
        print(L)
def bin_search(n: int, L: list = []) -> int:
    if not L:
        L = [1, 4, 5, 6, 10, 13, 15, 17, 18, 21, 29, 32, 34, 35, 37, 40, 46, 49, 53, 57, 100, 159, 205, 305, 400, 406, 506]

    left , right = 0, len(L) -1

    while left <= right:
        mid = (left + right ) // 2

        if L[mid] == n:
            return mid
        if L[mid] < n:
            left = mid + 1
        if L[mid] > n:
            right = mid - 1
    
    return -1

if __name__ == '__main__':
    result = binary_search(100)
    print("result = ", result)

