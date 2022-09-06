
def binary_search(li, x):
    left, right = 0, len(li) - 1
    
    while left <= right:
        mid = (left + right) // 2
    
        if li[mid] == x:
            return mid
        if li[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == "__main__":
    L = [1, 2, 3, 4, 6, 7, 8]

    for x in range(10):
        position = binary_search(L, x)

        if position == -1:
            if x in L:
                print(f"{x} is found in the list but binary_search() return -1")
            else:
                print(f"{x} not found in the list")
        else:
            if x not in L:
                print(f"{x} is not found but binary_search() returned a position for this")
            else:
                print(f"{x} found in the list")
            
        