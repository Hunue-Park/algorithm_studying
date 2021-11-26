# matrix product order
import sys
 
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(1, N): 
    for j in range(0, N-i):   
        dp[j][j+i] = 2**32 # 최댓값
        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])
            print(k+1, j+i, "k+1, j+i")

print(dp)