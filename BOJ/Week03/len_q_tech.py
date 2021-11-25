from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int,input().split())

graph = [[0]*c for _ in range(r)]

q_water = deque([])
q_Hedgehog = deque([])

for j in range(r):
    x = list(input().strip())
    for index, k in enumerate(x):
        if k == "*":
            graph[j][index] = -1
            q_water.append([j,index])
        elif k == "S":
            q_Hedgehog.append([j,index])
            graph[j][index] = 1
        elif k=='D':
            graph[j][index] = 'D'
            location_beaver = (j,index)
        elif k == "X":
            graph[j][index] = 'X'

dy = [1,0,-1,0]
dx = [0,1,0,-1]

while q_water or q_Hedgehog:
    for _ in range(len(q_water)):
        cy_water,cx_water = q_water.popleft()
        for i in range(4):
            ny_water , nx_water = cy_water+dy[i],cx_water+dx[i]
            if  0<=ny_water<r and 0<=nx_water<c and  graph[ny_water][nx_water] == 0:
                graph[ny_water][nx_water] = graph[cy_water][cx_water] - 1
                q_water.append([ny_water,nx_water])

    for _ in range(len(q_Hedgehog)):
        cy_Hedgehog,cx_Hedgehog = q_Hedgehog.popleft()
        for i in range(4):
            ny_Hedgehog , nx_Hedgehog = cy_Hedgehog+dy[i],cx_Hedgehog+dx[i]
            if 0<=ny_Hedgehog<r and 0<=nx_Hedgehog<c and  (graph[ny_Hedgehog][nx_Hedgehog] == 0 or graph[ny_Hedgehog][nx_Hedgehog] == 'D'):
                graph[ny_Hedgehog][nx_Hedgehog] = graph[cy_Hedgehog][cx_Hedgehog] + 1
                q_Hedgehog.append([ny_Hedgehog,nx_Hedgehog])


# print(*graph,sep="\n")
result = graph[location_beaver[0]][location_beaver[1]]
if result == "D":
    print("KAKTUS")
else:
    print(result-1)