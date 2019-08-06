from typing import List


def selection_sort(arr: List[int], desc: bool = False) -> List[int]:
    for j, item in enumerate(arr[:-1]):
        m: int = j
        for i, s_item in enumerate(arr[j:]):
            if (s_item < arr[m]) ^ desc:
                m = i + j
        arr[j], arr[m] = arr[m], arr[j]

    return arr
