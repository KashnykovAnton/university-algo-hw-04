import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def tim_sort(arr):
    return sorted(arr)

def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def run_tests():
    sizes = [100, 500, 1000]

    for size in sizes:
        test_data = generate_random_list(size)
        print(f"Sorting {size} elements:")

        insertion_time = timeit.timeit(lambda: insertion_sort(test_data), number=1)
        print(f"Insertion Sort Time: {insertion_time:.6f} sec")

        merge_time = timeit.timeit(lambda: merge_sort(test_data), number=1)
        print(f"Merge Sort Time: {merge_time:.6f} sec")

        timsort_time = timeit.timeit(lambda: tim_sort(test_data), number=1)
        print(f"Timsort Time: {timsort_time:.6f} sec")
        print("-" * 40)

if __name__ == "__main__":
    run_tests()