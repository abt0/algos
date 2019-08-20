from typing import List


def bubble_sort(arr: List[int], desc: bool = False) -> None:
    last: int = len(arr) - 1

    for i in range(0, last):
        for j in range(last, i, -1):
            if (arr[j] < arr[j - 1]) ^ desc:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
