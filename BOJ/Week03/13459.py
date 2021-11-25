# hide and seek 3

from collections import deque
import sys

input = sys.stdin.readline

def check_range(x):
    return (0 <= x < 100001)

def transposition(start, end):
    q.append(start)
    dist[start] = 0
    while q:
        now = q.popleft()
        if check_range(now * 2) and visited[now * 2] == 0:
            visited[now * 2] = 1
            q.appendleft(now * 2)
            dist[now * 2] = dist[now]

        if check_range(now - 1) and visited[now - 1] == 0:
            visited[now - 1] = 1
            q.append(now - 1)
            dist[now - 1] = dist[now] + 1
        if check_range(now + 1) and visited[now + 1] == 0:
            visited[now + 1] = 1
            q.append(now + 1)
            dist[now + 1] = dist[now] + 1
    print(dist[end])

if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [0] * 100001
    dist = [-1] * 100001
    q = deque()
    transposition(N, K)
