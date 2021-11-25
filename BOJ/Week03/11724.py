# conected component

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global cnt
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
    return 1

if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [0] * (N+1)
    for i in range(1, N+1):
        parent[i] = i
    rank = [1 for i in range(N+2)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(b, a)
    cnt = 0
    for i in range(1, N+1):
        if i == find(i):
            cnt += 1

    print(cnt)