# find the middle bidz.

import sys
from collections import deque
input = sys.stdin.readline


def more_less_count(target):
    q = deque()

    q.append(target)
    less_cnt = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            in_degree[i] -= 1
            q.append(i)
            less_cnt += 1
    
    q.append(target)
    more_count = 0
    while q:
        now = q.popleft()
        for i in reverse_graph[now]:
            out_degree[i] -= 1
            q.append(i)
            more_count += 1

    return less_cnt, more_count

N, M = map(int, input().split())
in_degree = [0] * (N+1)
out_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    in_degree[a] += 1
    out_degree[b] += 1
    graph[b].append(a)
    reverse_graph[a].append(b)


cnt = 0
for i in range(1, N+1):
    counts = more_less_count(i)
    if counts[0] > (N//2) or counts[1] > (N // 2):
        cnt += 1

print(cnt)
            