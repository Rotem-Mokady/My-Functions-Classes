from multiprocessing import pool, Manager
from datetime import datetime as dt
import types

class MultiTasking:
    """
    The class takes a bunch of functions and executes them at the same time in parallel.

    Signature:
        functions_list = []
        results = MultiTasking(functions_list).main()
        print(results)

    Parameters
    ----------
        func_list : list.
            The names of your functions in one list. The functions should be with no arguments at all.
        show_progress : bool, default -> True.
            True for watching the progress of the processes, False for not watching. It tells you how
            many functions haven't done their process yet. Example for print:
            *** 4 functions didn't finish the job, 66.66% done. ***
            That actually means 8 functions already finished their running.
        period : int, default -> 10.
            If you chose show_progress = True, the period is the number of seconds that You'll get your
            progress status.
            In default, you'll get the status every 10 seconds from the moment you started.

    Returns
    -------
        List of the outputs of your functions you put in 'func_list' parameter.
    """

    def __init__(self, func_list, show_progress=True, period=10):
        self.func_list = func_list
        self.show_progress = show_progress
        self.period = period
        self.result = None

    def run(self, func):
        return func()

    def main(self):
        self.error()  # if any argument is wrong.
        p = pool.ThreadPool() # get processors.
        Manager()  # sharing objects between processors.
        self.result = p.map_async(self.run, self.func_list, chunksize=1)
        # run, user functions and the number of functions in chunk.

        if self.show_progress: # Progress of the all processes together.
            self.Show_Status()

        output = self.result.get()  # actually the outputs of the user functions.
        p.close()  # no more task to that Pool for now.
        return output

    def Show_Status(self):
        printing = True
        start_time = dt.now()

        while not self.result.ready():  # bool value. True if it's done, False if it doesn't.
            time_delta = dt.now() - start_time
            time_delta = round(time_delta.total_seconds())
            # printing only once in the time range from the user.
            if self.period == 1:
                self.details()
            elif time_delta % self.period == 0 and printing:
                self.details()
                printing = False
            elif time_delta % self.period != 0 and not printing:
                printing = True

    def details(self):

        if self.result._number_left * self.result._chunksize > 1:
            status = str(self.result._number_left * self.result._chunksize) + " functions didn't finish the job, "
        else:
            status = str(self.result._number_left * self.result._chunksize) + " function didn't finish the job, "

        percentage = (1 - (self.result._number_left * self.result._chunksize) / len(self.func_list)) * 100

        if percentage % 1 == 0:
            percentage = str(int(percentage)) + '% done.'
        else:
            percentage = str(round(percentage, 2)) + '% done.'

        print("*** " + status + percentage + " ***")

    def error(self):
        if type(self.func_list) != list:
            raise ValueError('func_list must be a list.')
        for function in self.func_list:
            if type(function) != types.FunctionType:
                raise ValueError("'{}' is not a function.".format(str(function)))
            elif function.__code__.co_argcount > 0:
                raise ValueError("The functions should be with no arguments.'{}' has {} arguments."
                                 .format(str(function), function.__code__.co_argcount))
        if type(self.show_progress) != bool:
            raise ValueError('show_progress must be a bool.')
        if type(self.period) != int:
            raise ValueError('period must be an integer.')





num = 1000000000

def rotem():
    counter = 0
    for i in range(num):
        counter += i
    return {"rotem": counter}


def rotemm():
    counter = 0
    for i in range(num):
        counter += i
    return {"rotemm": counter == 123456789}


def rotemmo():
    counter = 0
    for i in range(num):
        counter += i
    return {"rotemmo": counter ** 0.5}


def rotemmok():
    counter = 0
    for i in range(num):
        counter -= i*2
    return {"rotemmok": counter}

if __name__ == '__main__':

    s1 = dt.now()
    func_list = [rotem, rotemm, rotemmo, rotemmok]
    multi_tasker = MultiTasking(func_list).main()
    print(multi_tasker)
    f1 = dt.now()
    t1 = f1 - s1
    print(t1.total_seconds(), 'seconds for parallel \n')

    s1 = dt.now()
    rotem()
    rotemm()
    rotemmo()
    rotemmok()
    f1 = dt.now()
    t1 = f1 - s1
    print(t1.total_seconds(), 'seconds for serial \n')



