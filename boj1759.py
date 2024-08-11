#!/usr/bin/python3
import sys


n, m = map(int, sys.stdin.readline().split())
w = sys.stdin.readline().split()
a = []
w.sort()

def backtrackking(c, v, vowel):
    if c >= n:
        if vowel > 0 and n - vowel >= 2:
            print("".join(a))
        return
        
    for i in range(v, m):
        if w[i] in a:
            continue
        l = len(a)
        a.append(w[i])
        backtrackking(c + 1, i, int(w[i] in ['a', 'e', 'o', 'u', 'i']) + vowel)
        a.pop(l)
        
for i in range(m):
    l = len(a)
    a.append(w[i])
    backtrackking(1, i, int(w[i] in ['a', 'e', 'o', 'u', 'i']))
    a.pop(l)
