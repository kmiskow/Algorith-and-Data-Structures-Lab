from kmp_find import find as find_kmp
from naive_find import find as find_naive
from kr_find import find as find_kr
import matplotlib.pyplot as plt
import gc
import time

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

def get_process_time(algorithm: callable, test_array,text):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for string in test_array:
        algorithm(string,text)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start

def performance_array(algorithm, array,text):
    time_values = []
    for size in range(100,1001,100):
        print("Size: ",size)
        test_array = array[:size].copy()
        time_values.append(get_process_time(algorithm, test_array,text))
    return time_values


def plotter(array,text):
    algorithm_data = {}

    algorithm_data["KMP"] = performance_array(find_kmp, array, text)
    print("KMP done!")
    algorithm_data["Naive"] = performance_array(find_naive, array, text)
    print("Naive done!")
    algorithm_data["KR"] = performance_array(find_kr, array, text )
    print("KR done!")
    x = list(range(100,1001,100))
    plot(x, algorithm_data, title="Sorting", xlabel="Array size", ylabel="Process time [s]")

with open(r'Patterns/pan-tadeusz.txt', encoding='UTF8') as f:
    contents = f.read()
    word_list = contents.split()
    plotter(word_list,contents)
    
