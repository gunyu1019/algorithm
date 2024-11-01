#!/usr/bin/python3
import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline()
    array_length = int(sys.stdin.readline())
    array = deque(sys.stdin.readline()[1:-2].split(','))
    
    # run command
    reverse = False
    for content in cmd:
        if content == 'R':
            reverse = not reverse
        elif content == 'D':
            if array_length <= 0 or len(array) <= 0:
                print('error')
                break 
            array_length -= 1    
            if reverse:
                array.pop()
            else:
                array.popleft()    
    else: 
        if reverse:
            array.reverse()
        print("[" + ",".join(array) + "]")
