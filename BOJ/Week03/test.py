from collections import deque
import sys
import heapq
input = sys.stdin.readline

class Solution():
    def __init__(self) -> None:
        N, K = map(int, input().split())
        maps = [list(map(int, input().split())) for _ in range(N)]
        sec, r, c = map(int, input().split())
        q = []
        visited = [[0]* N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if maps[i][j] != 0:
                    nums = maps[i][j]
                    heapq.heappush(q, (nums, (i, j)))
                    visited[i][j] = 1
        self.infectious(maps, N, visited, sec, q)
        print(maps[r-1][c-1])
    def check_range(x, y, N):
        return (0 <= x < N) and (0 <= y < N)

    def infectious(self, N, maps, visited, sec, q):
        time = 0
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            if time == sec:
                break
            sorted_q = deque()
            while q:
                sorted_q.append(heapq.heappop(q))
            while sorted_q:
                print(sorted_q)
                virus_num, (x, y)= sorted_q.popleft()
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if self.check_range(nx, ny, N) and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        maps[nx][ny] = virus_num
                        heapq.heappush(q, (virus_num, (nx, ny)))
            time += 1

Solution()