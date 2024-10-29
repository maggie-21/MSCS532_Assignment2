import random
import time
from memory_profiler import memory_usage

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    while left and right:
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))
    sorted_array.extend(left)
    sorted_array.extend(right)
    return sorted_array

def measure_performance(sort_function, data):
    start_time = time.time()  # Start time measurement
    mem_usage = memory_usage((sort_function, (data,)))  # Measure memory usage
    end_time = time.time()  # End time measurement
    execution_time = end_time - start_time  # Calculate execution time
    return execution_time, mem_usage

if __name__ == "__main__":
    # Generate test datasets
    dataset_sizes = [100, 1000, 5000, 10000]  # Adjust sizes as needed
    results = []

    for size in dataset_sizes:
        # Generate random dataset
        data = [random.randint(1, 10000) for _ in range(size)]

        # Measure performance for Quick Sort
        quick_sort_time, quick_sort_memory = measure_performance(quick_sort, data.copy())
        results.append({
            'size': size,
            'algorithm': 'Quick Sort',
            'execution_time': quick_sort_time,
            'memory_usage': quick_sort_memory[-1],  # Last recorded memory usage
        })

        # Measure performance for Merge Sort
        merge_sort_time, merge_sort_memory = measure_performance(merge_sort, data.copy())
        results.append({
            'size': size,
            'algorithm': 'Merge Sort',
            'execution_time': merge_sort_time,
            'memory_usage': merge_sort_memory[-1],  # Last recorded memory usage
        })

    # Print results
    print("Performance Results:")
    for result in results:
        print(f"Dataset Size: {result['size']}, Algorithm: {result['algorithm']}, "
              f"Execution Time: {result['execution_time']:.6f} seconds, "
              f"Memory Usage: {result['memory_usage']} MiB")
