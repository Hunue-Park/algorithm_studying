# algo spot

from collections import deque
import sys
input = sys.stdin.readline

def check_range(r, c):
    return (0 <= r < rows) and (0 <= c < cols)

def BFS(maps):
    # 어차피 시작점은 항상 동일 
    q.append([0, 0])
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while q:
        flag = 0
        r, c = q.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if check_range(nr, nc) and maps[nr][nc] == 0 and distances[nr][nc] == -1:
                q.appendleft([nr, nc])
                distances[nr][nc] = distances[r][c]
            elif check_range(nr, nc) and maps[nr][nc] == 1 and distances[nr][nc] == -1:
                q.append([nr, nc])
                distances[nr][nc] = distances[r][c] + 1
           

if __name__ == "__main__":
    cols, rows = map(int, input().split())
    maps = []
    for _ in range(rows):
        maps.append(list(map(int, input().strip())))
    distances = [[-1]* cols for _ in range(rows)]
    distances[0][0] = 0
    q = deque()
    BFS(maps)
    print(distances[-1][-1])
