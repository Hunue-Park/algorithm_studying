# minimum expanse 

import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

def dijkstra(graph, start):
    dist_list = {node: sys.maxsize for node in graph}
    dist_list[start] = 0
    q = []
    heapq.heappush(q, [dist_list[start], start])

    while q:
        cur_dist, cur_destin = heapq.heappop(q)
        if dist_list[cur_destin] < cur_dist:
            continue
        for new_destin, new_dist in graph[cur_destin].items():
            dist_var = cur_dist + new_dist
            if dist_var < dist_list[new_destin]:
                dist_list[new_destin] = dist_var
                heapq.heappush(q, [dist_var, new_destin])
    return dist_list

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    # 중첩 딕셔너리를 for 문으로 생성하기 위해서 두번째 키값에 해당하는 부분에 빈 딕셔너리를 만들어줘야함. 
    #graph = defaultdict(dict)  밑에서 이미 선언했으니 딱히 필요없음. 
    graph = {}
    for i in range(1, N+1):
        graph[i] = {}
    for _ in range(M):
        ### 진짜 말도안되는 반례 케이스가 있어,.,,,, 
        ## 딕셔너리 형태로 할때 가중치가 더 큰 간선이 나중에 입력되면 입력과정에서 갱신되버려서 
        # 연산 과정이 아무리 맞아도 통과가 안됨. 리스트로 입력을 받고 이후에도 append 사용해야 풀 수 있다. 
        a, b, c = map(int, input().split())
        graph[a][b] = c
    depart, landing = map(int, input().split())
    min_list = dijkstra(graph, depart)
    print(min_list[landing])
