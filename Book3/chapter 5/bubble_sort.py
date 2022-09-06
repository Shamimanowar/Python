"""
Complexity is O(n*n)
"""


def bubble_sort(li):
    n = len(li)

    for i in range(n - 1):
        worked = False
        for j in range(0, n - i - 1):
            print(li)
            if li[j] > li[j + 1]:
                worked = True
                li[j + 1], li[j] = li[j], li[j + 1]

        if not worked:
            break


if __name__ == "__main__":
    # L = [5, 3, 9, 1, 4, 0, 8]
    L = [0, 1, 3, 4, 5, 8, 9]
    print("Before sort: ", L)
    bubble_sort(L)
    print("After sort: ", L)
