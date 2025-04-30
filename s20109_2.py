import random
import time
import matplotlib.pyplot as plt

# Double-Ended Selection Sort Function
def double_ended_selection_sort(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        min_index = start
        max_index = start

        for i in range(start, end + 1):
            if arr[i] < arr[min_index]:
                min_index = i
            elif arr[i] > arr[max_index]:
                max_index = i

        if min_index != start:
            arr[start], arr[min_index] = arr[min_index], arr[start]
            if max_index == start:
                max_index = min_index

        if max_index != end:
            arr[end], arr[max_index] = arr[max_index], arr[end]

        start += 1
        end -= 1

    return arr

# Performance Analysis
def analyze_performance():
    input_sizes = [10, 50, 100, 500, 1000, 2000]
    runtimes = []

    for size in input_sizes:
        test_array = [random.randint(0, 10000) for _ in range(size)]
        start_time = time.perf_counter()
        double_ended_selection_sort(test_array)
        end_time = time.perf_counter()
        runtime_ms = (end_time - start_time) * 1000  
        runtimes.append(runtime_ms)
        print(f"Size: {size}, Time: {runtime_ms:.4f} ms")

    # Plotting
    plt.plot(input_sizes, runtimes, marker='o')
    plt.title('Performance of Double-Ended Selection Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Running Time (milliseconds)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_performance()
