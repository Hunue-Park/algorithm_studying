# sorting students
from collections import deque
import sys
input = sys.stdin.readline

def topologic_sort(graph, N):
    q = deque()
    result = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        current_student = q.popleft()
        result.append(current_student)
        for i in graph[current_student]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

if __name__ == "__main__":
    N, M = map(int, input().split())
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    topologic_sort(graph, N)



