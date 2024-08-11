#!/usr/bin/python3

import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

def quick_sort(arr, index = 0):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr)//2]
    less = []; more = []; equal = []
    for i, v in enumerate(arr):   
        if v < pivot:
            less.append(v)
        elif pivot < v:
            more.append(v)
    return quick_sort(less) + [pivot] + quick_sort(more)


a = {v: i for i, v in enumerate(quick_sort(x))}
for v in x:
    print(a[v], end=" ")
 
