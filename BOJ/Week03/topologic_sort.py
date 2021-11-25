# topology sort algorithm
# from collections import deque

# dq = deque()
# n = int(input()) # 그래프 정점의 수
# graph = [[] for _ in range(n+1)]
# indegree = [0] * (n+1)
# for i in range(n):
#     a, b = map(int, input().split())

#     graph[a].append(b)	#a는 b의 선행 노드
#     indegree[b] += 1	#b의 들어오는 간선의 수 추가

# # 들어오는 간선의 수가 0인 정점을 큐에 넣는다
# for i in range(1, n+1):
#     if not indegree[i]:
#         dq.append(i)

# for _ in range(1, n+1):
#     target = dq.popleft()
#     print(target)

#     # 선택한 정점과 연결된 정점의 간선을 삭제한다
#     for v in graph[target]:
#         indegree[v] -= 1
#         if not indegree[v]:
#             dq.append(v)
###################### que 이용 topological ################
# 그래프의 인접 행렬
graph = {0: [1, 2, 3], 1: [4], 2: [4, 5], 3: [], 4:[6], 5:[1], 6: []}

def topology_sort_stack(graph):
    N = len(graph)
    stack = [] # 스택
    visited = [0 for _ in range(N)] # 방문확인 리스트

    for i in graph:
        if visited[i] == 0:
            dfs(i, stack, visited)
            print(stack)
    
    answer = []
    while len(stack) != 0:
        # stack 에 담은 답을 pop 하는 것이기 때문에 
        # 호출 순서의 역순으로 최종 답이 만들어진다. 
        # 이는 위상정렬의 순서와 동일하다. 
        answer.append(stack.pop())
    print("최종 답 : ", answer)

def dfs(v, stack, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0: dfs(i, stack, visited)
    stack.append(v)

topology_sort_stack(graph)