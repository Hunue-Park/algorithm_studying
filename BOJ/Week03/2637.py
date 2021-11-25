# combine toies
from collections import defaultdict
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
        cur_num_q = deque()
        sub_result = []
        while q:
            cur_num_q.append(q.popleft())
        while cur_num_q:
            current_student = cur_num_q.popleft()
            for i in range(len(graph[current_student])):
                k = graph[current_student][i][0]
                indegree[k] -= 1
                if indegree[k] == 0:
                    sub_result.append(k)
                    cur_num_q.append(k)
                    print(sub_result)
        #print(sub_result)
        
    for i in result:
        print(i, end=' ')


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    indegree = [0] * (N+1)
    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[b].append((a, c))
        indegree[a] += 1
    # {1: [[5, 2]], 2: [[5, 2]], 5: [[7, 2], [6, 2]], 
    # 3: [[6, 3]], 4: [[6, 4], [7, 5]], 6: [[7, 3]]}
    topologic_sort(graph, N)
    #print(graph[1][0][0])


