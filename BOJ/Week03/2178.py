# searching maze
from collections import deque
import sys
input = sys.stdin.readline
# from safe area
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
### 원본 bfs ####### 
# def bfs(x, y):
#     q = deque()
#     q.append([x, y])
#     ch[x][y] = 1

#     while q:
#         a, b = q.popleft()

#         for i in range(4):
#             na = a + da[i]
#             nb = b + db[i]
#             if ch[na][nb] == 0:
#                 ch[na][nb] = 1
#                 q.append([na, nb])

# 여기다가 bfs(x, y) 자리에 (1, 1) 넣으면 될듯?
def bfs(x, y):
    q = deque()
    q.append([x, y])
    board[x][y] = 2

    while q:
        flag = 0
        a, b = q.popleft()

        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            # 여기다가 조건 추가하기. na, nb 가 N, M 이 되는 조건이면 break
            if 0 <= na < N and 0 <= nb < M:
                if board[na][nb] == 1:
                    board[na][nb] = 2
                    dis[na][nb] = dis[a][b] + 1
                    q.append([na, nb])
            if na == N-1 and nb == M-1:
                flag = 1
                break
        if flag == 1:
            break
    print(dis[N-1][M-1] + 1)
N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
dis = [[0] * M for _ in range(N)]
bfs(0,0)
