# Traveling Salesman Problem

import sys
input = sys.stdin.readline

def count(route, N):
    cnt = 0
    # 방문한 도시 개수를 카운트로 주는 듯
    for n in range(1, N):
        # 1<<n-1 ; 10000(n-1개의 0)
        # 겹치는 방문도시 경로가 있다면 
        if route & (1 << n - 1) != 0:
            # 카운트 + 1
            cnt += 1
    return cnt

def isin(i, route):
    # i 번째 도시에 방문 했다면 
    if route & ( 1 << i - 1) != 0:
        return True
    else:
        return False

def get_minimum(N, W, i, route, dp):
    minimum_dist = float('inf')
    for j in range(1, N):
        # j 번째 도시에 방문했었다면
        if isin(j, route):
            # j 번째를 제외한 방문 도시 경로가 바로 before_route 에 들어감
            before_route = route & ~(1 << j - 1)
            # dp 테이블 값의 의미는 j 번째부터 before경로를 거쳐 0까지 돌아오는 거리 
            dist = W[i][j] + dp[j][before_route]
            # 즉, 여기서 dist 는 i 부터 j 를 거쳐 before route 를 지나 0 으로 가는 거리를 의미. 
            if minimum_dist > dist:
                # 최솟값으로 갱신해주는 과정 
                minimum_dist = dist
    return minimum_dist

def solution(N, W, dp):
    # W 테이블을 inf 값으로 채운다.
    for i in range(N):
        for j in range(N):
            # 경로로 언급이 안되었다면 갈수 없는 것이므로 inf 값으로 초기화. 
            if not W[i][j]:
                W[i][j] = float('inf')
    # 각 i 번째 도시에서 0번째 도시로 돌아오는 최소값은 w 테이블의 값과 동일. 
    # => 어디 거쳐서 안간다는 말.
    for i in range(1, N):
        dp[i][0] = W[i][0]
    
    for k in range(1, N - 1):
        # route 가 비트마스크로 나타내지기 때문에 size 의 값은 
        # 2의 N-1 제곱의 크기를 가짐.
        for route in range(1, size):
            # N개의 도시중 루트에서 방문한 도시의 개수가 K개이면
            if count(route, N) == k:
                # 여기서 i 가 1부터이기 때문에 밑에 dp[0][size - 1] 은 따로 채워넣어야함
                for i in range(1, N):
                    # 루트에 i 번째 도시방문이 들어있지 않다면
                    if not isin(i, route):
                        # i 에서 루트 경로를 거쳐 0 으로 돌아오는 dp 테이블값 지정.
                        # 단 여기서 값을 넣을때 getminimum 함수로 최소값을 넣는다. 
                        dp[i][route] = get_minimum(N, W, i, route, dp)
    # 이 dp 칸은 위에서 다른 칸들이 다 채워져야 비로소 채워 넣을 수 있는 칸임. 
    dp[0][size - 1] = get_minimum(N, W, 0, size - 1, dp)
    return dp[0][size - 1]


if __name__ == "__main__":
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    size = 2 ** (N - 1)
    dp = [[float('inf')] * size for _ in range(N)]
    
    print(solution(N, W, dp))

