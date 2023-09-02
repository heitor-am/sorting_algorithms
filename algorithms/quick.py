import random

def quick_sort(arr, p, r):
    comparisons = 0

    if p < r:
        q, comp = partition(arr, p, r)
        comparisons += comp
        comparisons += quick_sort(arr, p, q - 1)
        comparisons += quick_sort(arr, q + 1, r)

    return comparisons

def partition(arr, p, r):
    comparisons = 0

    i = random.randint(p, r)
    arr[i], arr[r] = arr[r], arr[i]

    x = arr[r]
    i = p - 1
    for j in range(p, r):
        comparisons += 1

        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1, comparisons
