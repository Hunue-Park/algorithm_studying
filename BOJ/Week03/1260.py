# DFS and BFS
from collections import deque
import sys
input = sys.stdin.readline

def BFS(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

if __name__ == "__main__":
    n, m, v = map(int, input().split())

    graph = [[0] * (n+1) for _ in range(n + 1)]
    visit_list = [0] * (n + 1)
    visit_list2 = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
    
    dfs(v)
    print()
    BFS(v)









########## DFS 나쁘지 않았으 ############## 
# def DFS(start, tree, parents):
#     for i in tree[start]:
#         if parents[i] == 0:
#             parents[i] = start
#             out_orders.append(i)
#             DFS(i, tree, parents)
# if __name__ == "__main__":
#     N, M, V = map(int, input().split())
#     Tree = [[] for _ in range(N+1)]
#     Parents = [0 for _ in range(N+1)]
#     out_orders = []
#     out_orders_2 = []
#     for _ in range(M):
#         a, b = map(int, input().split())
#         Tree[a].append(b)
#         Tree[b].append(a)
#     Tree.sort()
#     DFS(V, Tree, Parents)
#     print(out_orders)