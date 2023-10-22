import random
import time
import gc
from tree import Tree
from avl_tree import avl_tree
from node import Node
import matplotlib.pyplot as plt
def get_insert_time(tree_type, array,lengths):
    result = []
    gc_old = gc.isenabled()
    for length in lengths:      
        gc.disable()   
        node = Node(length)
        t = tree_type(node)
        start = time.process_time()

        # ****************************
        for num in array[:length]:
            t.insert(num)
        # ****************************
       
        stop = time.process_time()
        result.append(stop - start) 
        print("For length ",length, " time: ",stop - start)
    if gc_old:
        gc.enable()
    return result
def get_find_time(tree_type, array,lengths):
    result = []
    gc_old = gc.isenabled()
    node = Node(10000)
    t = tree_type(node)
    for num in array:
        t.insert(num)
    for length in lengths:      
        gc.disable()   
        start = time.process_time()

        # ****************************
        for num in array[:length]:
            t.find(num)
        # ****************************
       
        stop = time.process_time()
        result.append(stop - start) 
        print("For length ",length, " time: ",stop - start)
    if gc_old:
        gc.enable()
    return result
def get_delete_time(tree_type, array,lengths):
    result = []
    gc_old = gc.isenabled()
    node = Node(10000)
    for length in lengths:      
        gc.disable()   
        t = tree_type(node)
        for num in array:
            t.insert(num)
        start = time.process_time()

        # ****************************
        for num in array[:length]:
            t.delete(num)
        # ****************************
       
        stop = time.process_time()
        result.append(stop - start) 
        print("For length ",length, " time: ",stop - start)
    if gc_old:
        gc.enable()
    return result

def plot(x, y,z=None, title="Title", xlabel="X", ylabel="Y"):  # either to png or show
    plt.title(title, fontsize='16')	 # title
    plt.plot(x, y)	 # plot the points  
    if z is not None:
        plt.plot(x, z)	 # plot the points
        plt.legend(labels=["Binary tree", "AVL Tree"],loc='best')
    else:
        plt.legend(labels=["Binary tree"],loc='best')
    plt.xlabel(xlabel, fontsize='13')  # adds a label in the x axis
    plt.ylabel(ylabel, fontsize='13')  # adds a label in the y axis
    # plt.legend(loc='best')  # creates a legend to identify the plot
    plt.savefig(title+'_'+xlabel+'_'+ylabel+'.png')	 # saves the figure in the present directory
    plt.grid()  # shows a grid under the plot
    # if show:
    #     plt.show()
def main():
    pass
if __name__ == "__main__":
    main()