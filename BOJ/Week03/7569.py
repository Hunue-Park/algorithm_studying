# Tomatoes
from collections import deque
import sys
input = sys.stdin.readline

def check_range(x, y, h):
    return (0 <= x < M) and (0 <= y < N) and (0 <= h < H)

def BFS(boxes):
    dx = [-1, 0, 0, 1, 0, 0]
    dy = [0, -1, 0, 0, 1, 0]
    dh = [0, 0, -1, 0, 0, 1]
    moves = [(-1,0,0), (0,-1,0), (0,0,-1), (1,0,0), (0,1,0), (0,0,1)]
    while q:
        h, y, x = q.popleft()
        for dx, dy, dh in moves:
            nx, ny, nh = x + dx, y + dy, h + dh
            if check_range(nx, ny, nh) and boxes[nh][ny][nx] == 0:
                q.append([nh, ny, nx])
                boxes[nh][ny][nx] = boxes[h][y][x] + 1
            

if __name__ == "__main__":
    M, N, H = map(int, input().split())
    boxes = [0] * H
    for i in range(H):
        boxes[i] = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] == 1:
                    q.append((i,j,k))
    BFS(boxes)
    check_tot = False
    result = -2

    for i in boxes:
        for j in i:
            for k in j:
                if k == 0:
                    check_tot = True
                result = max(result, k)
    if check_tot:
        print(-1)
    elif result == -1:
        print(0)
    else:
        print(result - 1)