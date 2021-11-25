import heapq

def dijkstra(graph, start):
    # start 로 부터의 거리값을 저장하기 위함. 가장 큰값으로 되어있기 때문에
    # 최솟값으로 지속적으로 갱신될것.
    dist_list = {node: float('inf') for node in graph} 
    # 자기자신까지의 거리는 0 
    dist_list[start] = 0
    queue = []
    # start 지점을 heap queue 에서 꺼내서 시작. 
    heapq.heappush(queue, [dist_list[start], start])
    
    while queue:
        # 큐에서 탐색할 노드와 거리를 꺼내온다.
        # 파이썬 자료구조상 최소힙으로 설정되어있기때문에 우선순위는 거리가 짧은 순서대로 들어가 있을것. 
        current_distance, current_destination = heapq.heappop(queue)
        # 꺼낸 노드까지의 거리가 현재 distances 에 저장되어있는 거리보다 길다면 
        if dist_list[current_destination] < current_distance:
            # 볼 필요도 없이 넘어감. 
            continue
        # 위조건문을 넘어왔다면 graph 딕셔너리의 current_destination 에 해당하는 index 에서 key 값과 value 를 다 꺼내준다. 
        for new_destination, new_distance in graph[current_destination].items(): 
            # 거리는 new_distance를 더해서 갱신. distance 라는 새로운 변수 선언 
            dist_var = current_distance + new_distance
            if dist_var < dist_list[new_destination]:
                dist_list[new_destination] = dist_var
                # 현재 노드의 다음 노드로의 인접거리를 계산하기위해 큐에 삽입. 
                heapq.heappush(queue, [dist_var, new_destination])
    
    return dist_list

if __name__ == "__main__":
    graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
    }

    print(dijkstra(graph, 'A'))