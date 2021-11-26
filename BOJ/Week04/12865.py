# knapsack algorithm

import sys
input = sys.stdin.readline

def knapsack_fn(N, K, knapsack, stuff):
    for i in range(1, N+1):
        for j in range(1, K+1):
            weight = stuff[i][0]
            value = stuff[i][1]
            # 현재 들어갈 j 가 물건의 무게보다 작으면 이전 dp 테이블의 값을 그대로 가져온다. 
            # 자신보다 윗 행, 동일한 열의 값을 가져옴 
            if j < weight:
                knapsack[i][j] = knapsack[i - 1][j]
            else:
                knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
    
    return knapsack[N][K]

if __name__ == "__main__":
    N, K = map(int, input().split())
    stuff = [[0, 0]]
    knapsack = [[0] * (K+1) for _ in range(N+1)]
    for _ in range(N):
        stuff.append(list(map(int, input().split())))
    
    print(knapsack_fn(N, K, knapsack, stuff))