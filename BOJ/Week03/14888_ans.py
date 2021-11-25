import sys
from typing import MappingView
input = sys.stdin.readline

def cal(num, idx, add, sub, multi, division):
    global n, maxv, minv 
    if idx == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        return
    else:
        if add:
            cal(num + num_list[idx], idx + 1, add-1, sub, multi, division)
        if sub:
            cal(num - num_list[idx], idx + 1, add, sub-1, multi, division)
        if multi:
            cal(num * num_list[idx], idx + 1, add, sub, multi - 1, division)
        if division:
            cal(int(num / num_list[idx]), idx + 1, add, sub, multi, division - 1)
    

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    maxv = -sys.maxsize - 1
    minv = sys.maxsize
    n = int(input())
    num_list = list(map(int, input().split()))
    a, b, c, d = map(int, input().split())
    cal(num_list[0], 1, a, b, c, d)
    print(maxv)
    print(minv)