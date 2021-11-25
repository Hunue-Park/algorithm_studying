# morning jogging 
from collections import defaultdict
import sys
input = sys.stdin.readline


def DFS(v, depth):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        # 실내에서 실내로 가게되면 cnt +=1 
        if in_out[v] and in_out[i] and depth == 0:
            cnt += 1
            continue
        # 실외에서 실내로 가게되면 cnt += 1
        # elif not in_out[v] and in_out[i]:
        #     cnt += 1
        #     continue
        # 다음 노드가 방문하지 않은 점이면 
        elif visited[i] == 0:
            # 실내에서 실외로 가는경우에는 DFS 로 들어감
            if in_out[v] and not in_out[i]:
                DFS(i, depth + 1)
            elif not in_out[v] and not in_out[i]:
                DFS(i, depth + 1)
            elif not in_out[v] and in_out[i]:
                cnt += 1
                continue
    return 


if __name__ == "__main__":
    N = int(input())
    cnt = 0
    in_out = [0] + list(map(int, input().strip()))
    graph = defaultdict(list)
    g_cnt = 0
    for _ in range(N-1):
        a, b = map(int, input().split())
        # 무방향 그래프 
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, N+1):
        visited = [0] * (N+1)
        if in_out[i] == 1:
            DFS(i, 0)

    print(cnt)