def insertion_sort(arr):
    for i, item in enumerate(arr):
        if i == 0:
            continue
        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = item
    return arr
