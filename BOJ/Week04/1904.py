# 0 tile

import sys 
input = sys.stdin.readline

N = int(input())
dp = [0] * 1000001
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    

print(dp[N])


############ 왜 이건 틀릴까 ############## 
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
    if dp[i] >= 15746:
        dp[i] = dp[i] % 15746

print(dp[N])