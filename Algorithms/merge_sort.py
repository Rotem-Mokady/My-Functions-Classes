import numpy as np


class MergeSort:
    """
    Specific class for merge sort method.
    """
    def __init__(self, array):
        self.array = [[i] for i in array]
        self.run = 0
        self.n = len(self.array)

    def switch(self, lst1, lst2):
        """
        The function takes two sorted lists and union them to one list.
        It also adds to self.run one point in any iteration for the efficiency check.
        """
        for i in range(len(lst1)):
            self.run += 1
            idx = 0
            for j in range(idx, len(lst2)):
                self.run += 1
                if lst1[i] < lst2[j]:
                    break
                if idx == len(lst2) - 1:
                    return lst2 + lst1[i:]
                idx += 1
            lst2 = lst2[:idx] + [lst1[i]] + lst2[idx:]

        return lst2

    def main(self):
        """
        The function sort an array with 'merge sort' method.
        The recursion is based on divided by two until we arrive to zero.
        """
        while self.n:
            self.n = round(self.n / 2)
            self.run += 1
            advanced = []
            for j in range(0, len(self.array), 2):
                self.run += 1
                try:
                    couple = self.switch(self.array[j], self.array[j+1])
                except IndexError:
                    couple = self.array[j]
                advanced.append(couple)
            self.array = advanced.copy()
        return self.run


class Sort:
    def __init__(self, array):
        self.array = array
        self.n = len(self.array)
        self.run = {
            'bubble sort': 0,
            'selection sort': 0,
            'quick sort': 0,
            'merge sort': 0,
        }

    def merge_sort(self):
        array = self.array.copy()
        run = MergeSort(array).main()
        self.run['merge sort'] = run
        return run


if __name__ == '__main__':

    a = np.random.randint(1, 100, np.random.randint(1, 100))
    print(Sort(a).merge_sort())