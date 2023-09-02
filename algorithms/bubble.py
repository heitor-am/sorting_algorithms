def bubble_sort(arr):
    comparisons = 0

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            comparisons += 1

            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return comparisons
