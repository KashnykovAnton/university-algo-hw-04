import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def compare_sorting_algorithms():
    # Generate random data
    data = [random.randint(0, 1000) for _ in range(1000)]
    
    # Merge sort
    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=100)
    
    # Insertion sort
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=100)
    
    # Timsort
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=100)
    
    print("Час сортування за допомогою сортування злиттям:", merge_sort_time)
    print("Час сортування за допомогою сортування вставками:", insertion_sort_time)
    print("Час сортування за допомогою Timsort:", timsort_time)

compare_sorting_algorithms()
