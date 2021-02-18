import numpy as np


class MergeSort:
    def __init__(self, array):
        self.array = array
        self.run = 0
        self.n = len(self.array)

    def switch(self, lst1, lst2):
        """
        The function takes two sorted lists and union them to one list.
        The function also adds to self.run in any iteration for the efficiency check.
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
        The function sort a list with 'Algorithms' method, according to
        recursion of divided by two.
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


def merge_sort(array):
    array = [[i] for i in array]
    run = MergeSort(array).main()
    # Set run results in the global dict
    return run


if __name__ == '__main__':

    a = np.random.randint(1, 100, np.random.randint(1, 100))
    print(merge_sort(a))