# kruskal algorithm 

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
    V, E = map(int, input().split())
    parent = [0] * (V+1)
    for i in range(1, V+1):
        parent[i] = i
    rank = [1 for i in range(V+2)]
    graph = []
    for _ in range(E):
        u, v, c = map(int, input().split())
        graph.append([u, v, c])
    graph.sort(key=lambda x: x[2])
    weight = 0
    for i in range(E):
        if find(graph[i][0]) != find(graph[i][1]):
            union(graph[i][1], graph[i][0])
            weight += graph[i][2]

    print(weight)


