def merge_sort(arr, p, r):
    comparisons = 0

    if p < r:
        comparisons += merge_sort(arr, p, (p + r) // 2)
        comparisons += merge_sort(arr, (p + r) // 2 + 1, r)
        comparisons += merge(arr, p, (p + r) // 2, r)

    return comparisons

def merge(arr, p, q, r):
    comparisons = 0

    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)

    for i in range(0, n1):
        left[i] = arr[p + i]

    for j in range(0, n2):
        right[j] = arr[q + j + 1]

    left[n1] = float('inf')
    right[n2] = float('inf')
    i = 0
    j = 0

    for k in range(p, r + 1):
        comparisons += 1

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

    return comparisons
