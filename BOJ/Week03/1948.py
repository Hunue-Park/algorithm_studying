# critical path 
from collections import deque
import sys
input = sys.stdin.readline

def find_max_cost(start, end):
    path_q.append(start)
    cost = [0] * (n+1)
    cost[start] = 0
    while path_q:
        now = path_q.popleft()
        for path in graph[now]:
            in_degree[path[0]] -= 1
            if in_degree[path[0]] == 0:
                path_q.append(path[0])
            if cost[path[0]] < (cost[now] + path[1]):
                cost[path[0]] = cost[now] + path[1]

    return cost

def reverse_path(end, cost):
    path_q.append(end)
    visited = [0] * (n+1)
    cnt = 0
    while path_q:
        now = path_q.popleft()
        visited[now] = 1
        for path in reverse_graph[now]:
            out_degree[path[0]] -= 1
            if cost[path[0]] == cost[now] - path[1]:
                cnt += 1
                if visited[path[0]] == 0:
                    visited[path[0]] = 1
                    path_q.append(path[0])
    print(cnt)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    in_degree = [0] * (n+1)
    out_degree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        in_degree[b] += 1
        out_degree[a] += 1
        graph[a].append([b,c])
        reverse_graph[b].append([a,c])

    start, end = map(int, input().split())
    path_q = deque()
    cost = [0] * (n+1)
    calculated_cost = find_max_cost(start, end)
    print(calculated_cost[end])
    reverse_path(end, calculated_cost)