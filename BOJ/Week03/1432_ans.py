#wodns's solution 

import sys
input = sys.stdin.readline
from heapq import heappop,heappush


def topology_sort():
    q = []
    for i in range(1,n+1):
        # 하나도 쏘는게 없으면 그 노드번호는 가장 우선순위가 높아짐. 최대힙. 
        if outdegree[i] == 0:
            heappush(q,-i)
            print(q, 'q 출력')
    N = n
    while q:
        now = -heappop(q)
        result[now] = N
        for k in graph[now]:
            outdegree[k] -= 1
            if outdegree[k] == 0:
                heappush(q,-k)

        N -= 1


n = int(input())

outdegree = [0]*(n+1)

result = [0]*(n+1)

graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    x = list(map(int,input().strip()))
    for j,k in enumerate(x):
        if k==1:
            graph[j+1].append(i)
            # 그래프에 위에 처럼 append 를 한다는거 자체가 
            # i 노드에서 j+1 노드로 outdegree 가 있다는것. 
            outdegree[i] +=1
print(graph)
print(outdegree)


topology_sort()

if result.count(0) > 1:
    print(-1)
else:
    print(*result[1:])