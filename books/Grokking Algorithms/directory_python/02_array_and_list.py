import numpy as np
import time
from numba import jit


def test_list() -> float:
    """
    Measures the time taken to iterate over a list of 1,000,000 elements.

    Returns:
        float: The processing time in seconds.
    """
    list_vector = range(1_000_000)

    start_time = time.time()
    for _ in list_vector:
        pass
    end_time = time.time()
    processing_time = end_time - start_time
    return processing_time


def test_array() -> float:
    """
    Measures the time taken to iterate over a numpy array of 1,000,000 elements.

    Returns:
        float: The processing time in seconds.
    """
    arr_vector = np.arange(1_000_000)

    start_time = time.time()
    for _ in arr_vector:
        pass
    end_time = time.time()
    processing_time = end_time - start_time
    return processing_time


def test_array_numba() -> float:
    """
    Measures the time taken to iterate over a numpy array of 1,000,000 elements
    using a function accelerated with Numba.

    Returns:
        float: The processing time in seconds.
    """
    @jit(nopython=True)
    def test_array_numba_inside(arr_vector: np.ndarray) -> None:
        """
        Numba-accelerated function to iterate over a numpy array.

        Args:
            arr_vector (np.ndarray): The numpy array to iterate over.
        """
        for _ in arr_vector:
            pass

    # Create the array outside the Numba function
    arr_vector = np.arange(1_000_000)

    # Measure the time taken to execute the Numba function
    start_time = time.time()
    test_array_numba_inside(arr_vector)
    end_time = time.time()

    processing_time = end_time - start_time
    return processing_time


if __name__ == '__main__':
    # Execute the test functions and print the results
    test_list_return = test_list()
    test_array_return = test_array()
    test_array_numba_return = test_array_numba()

    print(f'Time taken for list: {test_list_return:.10f} seconds.')
    print(f'Time taken for array: {test_array_return:.10f} seconds.')
    print(
        f'Time taken for array with Numba: {test_array_numba_return:.10f} seconds.')
