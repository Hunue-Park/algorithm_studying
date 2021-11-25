from collections import deque
import sys
input = sys.stdin.readline

def BFS(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visit_list[i] == 0:
                q.append(i)
                visit_list[i] = 1
                dis[i] = dis[v] + 1


if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visit_list = [0] * (N + 1)
    dis = [0] * (N+1)
    for _ in range(M):
            a, b = map(int, input().split())
            # 2차원 리스트 말고 무방향 그래프로 생성. 
            # undirected graph.
            #### 아니지. 이 문제는 단방향 그래프이기 때문에 무방향으로 그래프를 만들면 안돼!
            # 단방향 그래프 공부. 정리할 것. 
            graph[a].append(b)
            #graph[b].append(a)
    
    BFS(X)
    for i in range(N+1):
        if dis[i] == K:
            print(i)
    if K not in dis:
        print(-1)