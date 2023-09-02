def heapsort(arr):
    comparisons = 0

    build_max_heap(arr)
    heap_size = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        comp = max_heapify(arr, 0, heap_size)
        comparisons += comp

    return comparisons

def build_max_heap(arr):
    heap_size = len(arr)
    for i in range(len(arr) // 2, -1, -1):
        max_heapify(arr, i, heap_size)

def max_heapify(arr, i, heap_size):
    comparisons = 0

    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left
    if right < heap_size:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        comp = max_heapify(arr, largest, heap_size)
        comparisons += comp

    return comparisons
