from typing import List


def selection_sort(arr: List[int], desc: bool = False) -> None:
    for j in range(0, len(arr) - 1):
        m: int = j
        for i in range(j, len(arr)):
            if (arr[i] < arr[m]) ^ desc:
                m = i
        arr[j], arr[m] = arr[m], arr[j]
