# bipartite graph

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def DFS(v, color):
    visit_list[v] = color
    # 무방향 그래프로 만들어야 여기서 for 문 돌때 메모리 초과나 시간초과 안남.
    for i in graph[v]:
        # 방문한 곳이 아니면 
        if visit_list[i] == 0:
            # 이건 재귀로 들어갔다가 하나라도 False 나오면 그대로 쭉 탈출하기 위한 장치가 아닐까 
            # not DFS 라는게 False를 받아오면 이라는 것 같은데. not False 즉 True 일때 return False 다시 한다.
            if not DFS(i, -color):
                return False
        # 방문한 곳이 아닌데 => 다른 for 문을 돌때, 혹은 다른 노드와 인접하여 이미 방문처리가 되었는데
        # 동일한 color 라면 False 를 리턴. 
        elif visit_list[i] == visit_list[v]:
            return False
        # 방문한 곳이면 그냥 return True 
    return True


if __name__ == "__main__":
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V + 1)]
        visit_list = [0] * (V + 1)
        for _ in range(E):
            a, b = map(int, input().split())
            # 2차원 리스트 말고 무방향 그래프로 생성. 
            # undirected graph.
            graph[a].append(b)
            graph[b].append(a)
        bipartite = True
        for i in range(1, V+1):
            if visit_list[i] == 0:
                bipartite = DFS(i, 1)
                if not bipartite:
                    break
    
        print("YES" if bipartite else "NO")
