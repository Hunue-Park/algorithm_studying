# zxcasd 3004 code

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
in_degree = [0] * (n+1)
out_degree = [0] * (n+1)
arr = [[] for _ in range(n+1)]
revers_arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    in_degree[b]+=1
    out_degree[a]+=1
    arr[a].append([b,c])
    revers_arr[b].append([a,c])

start, end = map(int, sys.stdin.readline().split())

q = deque()
q.append(start)

cost = [0] * (n+1)
cost[start] = 0
print(arr)
while q:
    now = q.popleft()
    # print(now)
    # print('in', in_degree)
    # print('out', out_degree)
    # print(cost)
    for i in arr[now]:
        in_degree[i[0]] -= 1
        # print(now, i)
        if in_degree[i[0]] == 0 :
            q.append(i[0])
        # 가는데 드는 비용의 최대값 갱신. 
        if cost[i[0]] < (cost[now] + i[1]):
            cost[i[0]] = cost[now] + i[1]


print(cost[end])

q.append(end)
visited = [False] * (n+1)

cnt = 0
while q:
    now = q.popleft()
    visited[now]=True
    for i in revers_arr[now]:
        out_degree[i[0]] -= 1
        # cost 에 저장된 해당 노드까지의 값(=> 최대값을 만들어내는 값) 과 cost[now] - i[1] 를 비교해서 같으면
        # 이는 해당 노드가 최대 경로를 통과하는 경로임을 의미한다. 
        if cost[i[0]] == cost[now] - i[1]:
            # print(now, i)
            cnt+=1
            if visited[i[0]] == False:
                visited[i[0]] = True
                q.append(i[0])
    # print(q)
print(cnt)