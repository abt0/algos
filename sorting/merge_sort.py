from typing import List


# O(n lg n) Divide-and-Conquer
def merge_sort(arr: List[int], desc: bool = False) -> None:
    if len(arr) > 1:
        q = len(arr) // 2

        l_arr, r_arr = arr[:q], arr[q:]

        merge_sort(l_arr, desc)
        merge_sort(r_arr, desc)

        i = j = k = 0

        while i < len(l_arr) and j < len(r_arr):
            if (l_arr[i] < r_arr[j]) ^ desc:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1
