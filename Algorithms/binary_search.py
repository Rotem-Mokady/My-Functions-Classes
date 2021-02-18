import numpy as np
from copy import deepcopy


def binary_search(number, array):
    array = sorted(array)

    left_idx = 0
    right_idx = len(array)
    mid_idx = round((left_idx + right_idx) / 2)
    if array[mid_idx] == number:
        return True

    while mid_idx not in (0, len(array) - 1):
        if number > array[mid_idx]:
            left_idx = deepcopy(mid_idx)
        else:
            right_idx = deepcopy(mid_idx)
        mid_idx = round((left_idx + right_idx) / 2)
        if array[mid_idx] == number:
            return True
    return False


if __name__ == '__main__':

    a = np.random.randint(1, 10, 10)
    print(sorted(a))
    print("*************************")
    print(binary_search(9, a))
