# making maize
import heapq
import sys
input = sys.stdin.readline

def check_range(x, y):
    return (0 <= x < N) and (0 <= y < N)


def dijkstra(x, y):
    hq = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = [[0]* N for _ in range(N)]
    heapq.heappush(hq, (0, x, y))
    visited[x][y] = 1
    while hq:
        weight, cx, cy = heapq.heappop(hq)
        if cx == N - 1 and cy == N - 1:
            return weight
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if check_range(nx, ny) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if board[nx][ny]:
                    heapq.heappush(hq, (weight, nx, ny))
                else:
                    heapq.heappush(hq, (weight + 1, nx, ny))

if __name__ == "__main__":
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip())))
    answer = dijkstra(0, 0)
    print(answer)
    