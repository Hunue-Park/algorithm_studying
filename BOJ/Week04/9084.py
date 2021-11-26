# coins feat. knapsack algorithm

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N = int(input())
    coins = list(map(int, input().split))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    # 0을 만드는 경우는 무조건 1. j-i 가 0이될때 0이되는 경우를 합쳐줘야하기 때문.
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    print(dp[M])