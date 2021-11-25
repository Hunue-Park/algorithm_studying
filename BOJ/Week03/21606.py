# DFS의 본질. 빠짐없이 탐색하는 기능에 집중. 





from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def DFS(graph, node, inout, count = 0):
    if inout[node] == 2:
        return count
    if inout[node] == 1:
        return count + 1
    inout[node] = 2
    ############### 이부분이랑
    for i in graph[node]:
        if inout[i] == 2:
            continue
        count = DFS(graph, i, inout, count)
    return count

def count_route(n, graph, inout):
    count = 0
    for start_node in range(1, n + 1):
        if inout[start_node] == 0:
            outdoors = DFS(graph, start_node, inout)
            count += outdoors * (outdoors-1)
    for start_node in range(1, n+1):
        if inout[start_node] == 1:
            # 여기서 방문 처리를 안하는 이유는 인접노드에서 출발하여 해당 노드로 왔을때
            # 개수를 세야하기 때문. 방문처리 2 를 해버리면 아예 count 가 증가하지 않게된다. 
            inout[start_node] = 0
            outdoors = DFS(graph, start_node, inout)
            count += 2 * outdoors
    return count 




if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline
    N = int(input())
    inout = [0] + list(map(int, input().strip()))
    graph = defaultdict(list)
    # route_count = 0 # n*(n-1)을 갱신하는 변수; 이 변수는 count_route 함수 내부의 
    # count 변수에 의해 대체된다. 꼭 글로벌로 변수를 실행할 필요가 없다.
    for _ in range(N-1):
        a, b = map(int, input().split())
        # 무방향 그래프
        graph[a].append(b)
        graph[b].append(a)
    print(count_route(N, graph, inout))