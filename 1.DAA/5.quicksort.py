import random
import time

def quick_sort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # last element as pivot
    left  = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x >  pivot]
    return quick_sort_deterministic(left) + [pivot] + quick_sort_deterministic(right)

def quick_sort_randomized(arr):
    if len(arr) <= 1:
        return arr
    pivot  = arr[random.randint(0, len(arr) - 1)]  # random pivot
    left   = [x for x in arr if x <  pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x >  pivot]
    return quick_sort_randomized(left) + middle + quick_sort_randomized(right)

def analyze_sorting():
    # --- User Input ---
    n = int(input("Enter number of elements: "))
    arr = []

    print("Enter array elements:")
    for i in range(n):
        val = int(input(f"Element {i+1}: "))
        arr.append(val)

    print("\nOriginal array:", arr)

    # --- Deterministic QuickSort ---
    start = time.time()
    sorted_det = quick_sort_deterministic(arr.copy())
    end = time.time()
    t_det = end - start

    print("\nDeterministic QuickSort result:", sorted_det)
    print(f"Time taken by Deterministic QuickSort: {t_det:.6f} seconds")

    # --- Randomized QuickSort ---
    start = time.time()
    sorted_rand = quick_sort_randomized(arr.copy())
    end = time.time()
    t_rand = end - start

    print("\nRandomized QuickSort result:", sorted_rand)
    print(f"Time taken by Randomized QuickSort: {t_rand:.6f} seconds")

# --- Run Program ---
analyze_sorting()

#Theory
Quick Sort is a divide-and-conquer sorting algorithm that works by selecting a pivot element, partitioning the array into two subarrays — one with elements less than the pivot and one with elements greater — and then recursively sorting these subarrays.

⚙️ 1. Deterministic Quick Sort

Pivot Selection: Always chooses a fixed position pivot (e.g., last or first element).

Drawback: For already sorted or nearly sorted input, it can lead to unbalanced partitions, causing poor performance.

🎲 2. Randomized Quick Sort

Pivot Selection: Chooses a pivot randomly from the array.

Advantage: Reduces the chance of worst-case behavior and ensures average-case efficiency regardless of input order.

quick sort- Time complexity - 0(nlogn) space complxity-O(log n )