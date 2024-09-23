import numpy as np
import time
import pandas as pd


def linear_search(arr: np.array, target: int) -> int:
    """
    Perform a linear search on the given array to find the target element.

    Parameters:
    arr (np.array): The array to be searched. It should be an instance of numpy.array.
    target (int): The element to be searched for. It should be an integer.

    Returns:
    int: The index of the target element if found, None otherwise. This function returns an integer index if the target is found, otherwise, it returns None.
    """
    for i in range(arr.size):
        if arr[i] == target:
            return i
    return None


def binary_search(arr: np.array, target: int) -> int:
    """
    Perform binary search on a sorted array to find the index of the target element.

    Parameters:
    arr (np.array): The sorted array to search in. This array must be sorted and of type numpy.array.
    target (int): The element to search for. The target must be an integer.

    Returns:
    int: The index of the target element in the array, or None if the element is not found. This function returns an integer index if the target is found in the sorted array, otherwise, it returns None.
    """
    low = 0
    high = arr.size-1
    while low <= high:
        mid = (low+high)//2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':

    arr = np.arange(1_000_000)
    target = 567

    start_time_linear = time.time()
    (linear_search(arr, target))
    end_time_linear = time.time()
    processing_time_linear = end_time_linear - start_time_linear

    print(f'{processing_time_linear:.10f} seconds.')

    start_time_binary = time.time()
    (binary_search(arr, target))
    end_time_binary = time.time()
    processing_time_binary = end_time_binary - start_time_binary
    print(f'{processing_time_binary:.10f} seconds.')

    if processing_time_binary == 0:
        times_faster = np.inf
    else:
        times_faster = processing_time_linear/processing_time_binary

    print(
        f'Binary search is {times_faster:.2f} times faster than linear search.')

    with open('data/binary_search.log', 'a') as f:
        f.write(str(times_faster))
        f.write('\n')
        f.close()

    df = pd.read_csv('data/binary_search.log', header=None)
    print(df.describe())
