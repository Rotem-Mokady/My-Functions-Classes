from pprint import pprint
import numpy as np


LETTERS = [chr(char) for char in range(ord('a'), ord('f'))]
NUMBERS = range(1, 8)


def create_dict(workers, jobs):

    def set_workers():
        length = len(workers)
        idxs = np.random.randint(1, length)
        return list(set(map(lambda x: workers[x], np.random.randint(length, size=(idxs)))))

    return {job: set_workers() for job in jobs}


def cross_dicts(dict1, dict2):

    assert len(dict1) == 1, "dictionary should be with only one key. {param} got {length} keys.".format(
        param=dict1,
        length=len(dict1))

    assert isinstance(dict1, dict), "dict1 must be a dict."

    assert len(dict2) == 1, "dictionary should be with only one key. {param} got {length} keys.".format(
        param=dict2,
        length=len(dict2))

    assert isinstance(dict2, dict), "dict2 must be a dict."

    key1 = list(dict1.keys())[0]
    key2 = list(dict2.keys())[0]

    return [{key1: val1, key2: val2} for val1 in list(dict1.values())[0] for val2 in list(dict2.values())[0]]


if __name__ == '__main__':
    job2workers = create_dict(LETTERS, NUMBERS)
    max_jobs = max([len(val) for val in job2workers.values()])
    #
    pprint(job2workers)
    # print(max_jobs)
    print("**************************************")
    # my_dict = [{i: j} for i, j in job2workers.items()]
    # pprint(cross_dicts(my_dict[0], my_dict[1]))

    for i in range(max_jobs):
