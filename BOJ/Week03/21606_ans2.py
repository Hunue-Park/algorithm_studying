import sys 
from collections import defaultdict

def dfs(graph, node, inout, count=0):
    if inout[node] == 2:
        return count 
    # 실내에서 DFS 를 시작할 경우 주변 실내 1개를 세고 함수값 리턴. 
    if inout[node] == 1:
        return count + 1 
    # 여기서 visited 리스트랑 inout 리스트를 함께 사용하는구나. 
    # 2는 방문. 1은 실내. 0은 실외. 어차피 한번 방문하면 안가도 되니까
    # 이 DFS 로 주변 실내 노드를 세는구나. 
    inout[node] = 2
    ############### 이부분의 차이 ##################
    for next_node in graph[node]:
        if inout[next_node] == 2:
            continue
        count = dfs(graph, next_node, inout, count)
    return count 
    ########################################

# DFS 함수에서 count 를 함수결과값으로 리턴하고 
# count_path 함수에서 받은 count 를 가지고 route 의 개수를 계산. 
def count_path(n, graph, inout):
    count = 0
    # 실외끼리 붙어있는 경우든 실내 끼리 붙어있든 결국 시작점이 중요하기때문에 
    # 시작점에따라 구분하고 맨 처음 시작을 전체 노드에서 돌린다.
    # 여기 for 문에서 O(N) 만큼 사용.  
    for start_node in range(1, n+1):
        if inout[start_node] == 0:
            outdoors = dfs(graph, start_node, inout)     
            count += outdoors * (outdoors-1)
    for start_node in range(1, n+1):
        if inout[start_node] == 1:
            inout[start_node] = 0
            outdoors = dfs(graph, start_node, inout)     
            count += 2 * outdoors
    return count


if __name__ == '__main__':
    sys.setrecursionlimit(100000000)
    input = sys.stdin.readline
    n = int(input())
    inout = list(map(int, '0' + input().rstrip()))
    
    graph = defaultdict(list)
    for _ in range(n-1):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)
    print(count_path(n, graph, inout))
    

