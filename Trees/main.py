import random
from tree import Tree
from avl_tree import avl_tree
import matplotlib.pyplot as plt
from time_n_plot import *


def main():
    # Base variables
    randomlist = random.sample(range(1, 30000), 10000)
    n = [1000* i for i in range(1,11)]

    # Time actions
    print("Time insertion for:")
    print("Binary Tree")
    times = get_insert_time(Tree,randomlist,n)
    print("AVL Tree")
    times2 = get_insert_time(avl_tree,randomlist,n)
    print("Time finding for:")
    print("Binary Tree")
    times3 = get_find_time(Tree,randomlist,n)
    print("AVL Tree")
    times4 = get_find_time(avl_tree,randomlist,n)
    print("Time deletion")
    times5 = get_delete_time(Tree,randomlist,n)

    # Plot results
    plt.figure(1)
    plot(n,times,times2,title= "Insertion",xlabel="Array Size",ylabel="Time")
    plt.figure(2)
    plot(n,times3,times4, title="Finding",xlabel="Array Size",ylabel="Time")
    plt.figure(3)
    plot(n,times5, title="Deletion",xlabel="Array Size",ylabel="Time")
    plt.show()
    

if __name__ == "__main__":
    main()
