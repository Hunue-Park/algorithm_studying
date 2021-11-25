# melting ice 
import sys


def DFS(sea_table):
    visited = [[0] * M for _ in range(N)]
    count = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            # 빙산의 높이 남아있는 지점이 있는데 방문하지 않았다
            # => melting 으로 도달 할 수 없는, 즉 단절된 빙산이라는 의미
            if sea_table[i][j] > 0 and not visited[i][j]:
                # 빙산개수 카운팅
                count += 1
                # 해당 지점에서 melting 다시 실행. 왜??? 애초에 맨 처음 melting 을 
                # 아직 한번도 안한상태에서 들어오게 될 것이므로 melting 을 한번 쭉 돌고나서 count 는 1 이다. 
                # 그런데 이후에 while 문 안에서 DFS 가 다시 실행되게 되면 sea_table 이 바뀌고 나서 다시 도는것이므로.
                melting(sea_table, i, j, visited)
    return count 

def melting(sea_table, x, y, visited):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and sea_table[nx][ny] == 0 and not visited[nx][ny]:
            sea_table[x][y] = max(0, sea_table[x][y] - 1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and sea_table[nx][ny] and not visited[nx][ny]:
            melting(sea_table, nx, ny, visited)



    
if __name__ == "__main__":
    sys.setrecursionlimit(10**8)
    input = sys.stdin.readline
    N, M = map(int, input().split())
    sea_table = [list(map(int, input().split())) for _ in range(N)]
    year = -1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while True:
        num_part = DFS(sea_table)
        print(num_part, 'num part')
        year += 1
        if num_part > 1:
            break
        if num_part == 0:
            year = 0
            break
    print(year)