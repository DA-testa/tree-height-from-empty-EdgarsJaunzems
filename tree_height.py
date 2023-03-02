# python3

import sys
import threading


def compute_height(n, parents):
    h = [-1] * n
    # Write this function
    def cal(node):
        if h[node] != -1:
            return h[node]
        if parents[node] == -1:
            h[node] = 1
        else:
            h[node] = aprekins(parents[node]) + 1
        return h[node]
    max_height = 0
    # Your code here
    for a in range(n):
        max_height = max(max_height, aprekins(a))
    return max_height


def main():
    # implement input form keyboard and from files
    inputs = str(input())
    # let user input file name to use, don't allow file names with letter a
    if "I" in inputs:
        d = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(d, parents)
        print(height)
    elif "F" in inputs:
        name = input()
        if "test/" not in name:
            name = "test/" + name
        if "test/" in name:
            with open(name) as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
                height = compute_height(n, parents)
                print(height)
        if "a" in name:
            return

    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
