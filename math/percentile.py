from typing import List


def percentile(arr: List[int], percentile_rank: int) -> int:
    arr.sort()

    i = percentile_rank * (len(arr)-1) // 100

    return arr[i]


def median(arr: List[int]) -> int:
    return percentile(arr, 50)

