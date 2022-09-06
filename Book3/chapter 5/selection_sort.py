"""Time complexity of selection sort is O(n*n)"""


def selection_sort(li):
    n = len(li)

    for i in range(n-1):
        index_min = i

        for j in range(i + 1, n):
            if li[index_min] > li[j]:
                index_min = j

        if index_min != i:
            li[i], li[index_min] = li[index_min], li[i]


if __name__ == "__main__":
    L = [3, 4, 1, 9, 0, 5]
    print(f"Before sort: {L}")
    selection_sort(L)
    print(f"After sort: {L}")
