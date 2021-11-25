# black wizard lee

from collections import deque
import sys
input = sys.stdin.readline

def check_range(r, c):
    return (0 <= r < rows) and (0 <= c < cols)

def escape(board, gos_q, water_q):
    rows = len(board)
    cols = len(board[0])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    for r, c in water_q + gos_q:
        visited[r][c] = True
    
    time = 0
    while gos_q:
        time += 1
        cur_gos_q = deque()
        # 이 while 문은 gos_q 에있는 성분을 다 빼내기 위함.
        while gos_q:
            cur_gos_q.append(gos_q.popleft())
        # gos_q 에서 다 커낸 원소들로 while 문 시작. 
        while cur_gos_q:
            r, c = cur_gos_q.popleft()
            # 현재 고슴도치 좌표가 * 에 있으면
            if board[r][c] == 2:
                # while문과 상호작용 하지 않는다. 
                continue
            # 위치 변화량 
            for dr, dc in moves:
                # 한 턴 뒤의 좌표
                nr, nc = r + dr, c + dc
                if check_range(nr, nc) and not visited[nr][nc]:
                    # 방문 표시. 
                    visited[nr][nc] = True
                    # 방문할 좌표가 . 이면 
                    if board[nr][nc] == 3:
                        # 고슴도치의 queue 에 그 좌표를 넣는다. (다시 while문을 돌려야하니)
                        gos_q.append((nr, nc))
                    # 비버굴에 도달하면 지금까지 몇번 움직였는지 카운트하던 time 변수를 
                    # 결과값으로 리턴한다. 
                    if board[nr][nc] == 0:
                        return time
        # 왜 cur_water 를 새로 만들어야하는가? 
        # time 변수 카운팅을 하기 위함. 한번 움직일때 cur를 다 비우고 다시채울때 바로 cur 로 채우는게 아니라
        # 이전 q 로 채우기때문에 한번 4방향으로 다 움직이고 time 카운팅한다음에 다시 cur 를 채워서
        # 탐색을 이어나간다. 즉, 한번 한번 움직이는 과정을 체크하고 싶을때 사용. 
        cur_water_q = deque()
        while water_q:
            cur_water_q.append(water_q.popleft())
        while cur_water_q:
            r, c = cur_water_q.popleft()
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if check_range(nr, nc):
                    if board[nr][nc] == 3:
                        board[nr][nc] = 2
                        water_q.append((nr, nc))
    # 'D' 에 도달하지 않고 여기까지 온다면 도달 할 수 없다는 뜻이므로 
    # kaktus 리턴. 
    return 'KAKTUS'

def letter_to_digit(letter):
    map_dict = {'D': 0, 'S': 1, '*': 2, '.': 3, 'X': 4}
    return map_dict[letter]




if __name__ == "__main__":
    rows, cols = map(int, input().split())
    board = [[0] * cols for _ in range(rows)]
    gos_q = deque()
    water_q = deque()
    for r in range(rows):
        # 와 형변환을 함수로도 할 수 있구나. 
        one_row = list(map(letter_to_digit, input().rstrip()))
        for c in range(cols):
            board[r][c] = one_row[c]
            if one_row[c] == 1:
                gos_q.append((r, c))
            elif one_row[c] == 2:
                water_q.append((r, c))
    print(escape(board, gos_q, water_q))

################################################### 코드 창고 ################################
# while q_water or q_Hedgehog:
#     for _ in range(len(q_water)):
#         cy_water,cx_water = q_water.popleft()
#         for i in range(4):
#             ny_water , nx_water = cy_water+dy[i],cx_water+dx[i]
#             if  0<=ny_water<r and 0<=nx_water<c and  graph[ny_water][nx_water] == 0:
#                 graph[ny_water][nx_water] = graph[cy_water][cx_water] - 1
#                 q_water.append([ny_water,nx_water])

#     for _ in range(len(q_Hedgehog)):
#         cy_Hedgehog,cx_Hedgehog = q_Hedgehog.popleft()
#         for i in range(4):
#             ny_Hedgehog , nx_Hedgehog = cy_Hedgehog+dy[i],cx_Hedgehog+dx[i]
#             if 0<=ny_Hedgehog<r and 0<=nx_Hedgehog<c and  (graph[ny_Hedgehog][nx_Hedgehog] == 0 or graph[ny_Hedgehog][nx_Hedgehog] == 'D'):
#                 graph[ny_Hedgehog][nx_Hedgehog] = graph[cy_Hedgehog][cx_Hedgehog] + 1
#                 q_Hedgehog.append([ny_Hedgehog,nx_Hedgehog])
#### q가 다 빌때 까지 반복문을 도는것이 아니라 처음 q_water 의 길이만큼 돈다. 
## => 그러면 따로 q 를 만들지 않아도 가능. 