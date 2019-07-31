from typing import List


# O(n^2)
def insertion_sort(arr: List[int], desc: bool = False) -> List[int]:
    for i, item in enumerate(arr):
        if i == 0:
            continue
        j: int = i - 1
        while j >= 0 and (arr[j] > item) ^ desc:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
    return arr
