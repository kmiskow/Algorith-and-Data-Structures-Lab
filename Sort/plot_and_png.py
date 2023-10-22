import time
import gc
import matplotlib.pyplot as plt
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def plot(x, y, show=True, title="Title", xlabel="X", ylabel="Y"):  # either to png or show
    plt.title(title, fontsize='16')	 # title
    for name, values in y.items():
        plt.plot(x, values, label=name)	 # plot the points
    plt.xlabel(xlabel, fontsize='13')  # adds a label in the x axis
    plt.ylabel(ylabel, fontsize='13')  # adds a label in the y axis
    plt.legend(loc='best')  # creates a legend to identify the plot
    plt.savefig(title+'_'+xlabel+'_'+ylabel+'.png')	 # saves the figure in the present directory
    plt.grid()  # shows a grid under the plot
    if show:
        plt.show()


def get_process_time(algorithm: callable, array):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    algorithm(array)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def performance_array(algorithm, array, range_stop, step):
    time_values = []
    for size in range(0, (range_stop+1), step):
        test_array = array[100:(100+size)].copy()
        time_values.append(get_process_time(algorithm, test_array))
    return time_values


def plotter(array, range_stop, range_step):
    algorithm_data = {}

    algorithm_data["bubble sort"] = performance_array(bubble_sort, array, range_stop, range_step)
    print("Bubble sort done!")
    algorithm_data["selection sort"] = performance_array(selection_sort, array, range_stop, range_step)
    print("Selection sort done!")
    algorithm_data["insertion sort"] = performance_array(insertion_sort, array, range_stop, range_step)
    print("Insertion sort done!")
    algorithm_data["merge sort"] = performance_array(merge_sort, array, range_stop, range_step)
    print("Merge sort done!")
    algorithm_data["quick sort"] = performance_array(quick_sort, array, range_stop, range_step)
    print("Quick sort done!")

    x = list(range(0, range_stop+1, range_step))
    plot(x, algorithm_data, title="Sorting", xlabel="Array size", ylabel="Process time [s]")
