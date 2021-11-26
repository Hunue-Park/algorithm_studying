# longest subsequence
import bisect

# N = int(input())
# nums = list(map(int, input().split()))

# dp = [nums[0]]

# for i in range(N):
#     if nums[i] > dp[-1]:
#         dp.append(nums[i])
#     else:
#         idx = bisect.bisect_left(dp, nums[i]) 
#         #현재위치가 이전위치보다 작거나 같으면 bisect로 이전 위치의 원소중 가장 큰 원소의 idenx값을 구한다. 
#         dp[idx] = nums[i]
#         #그리고 dp의 index원소를 arr[i] 로 바꿔준다. 
########## bisect 을 사용했기 때문에 시간복잡도에서 훨씬 이득이 있으며 N <= 10**10 인 경우까지 커버가능 O(logN) 이니까
# print(len(dp))        

# 근데 이건 길이만 구하는 거라 상관이 없지만 => 어차피 마지막 값보다 작은 값이 새로 들어와도 그 수와 동일한 크기 관계를 가지는 
# 리스트의 위치에 집어넣으면 되기때문에 크게 상관이 없다. (길이는 동일하게 유지된다.)
# 아예 그 수열을 구하라고 하면 어떻게 할까 
### 길이만 구하는 다른 방법 ##################################
x = int(input())                                      
arr = list(map(int, input().split()))                  
                                                       
dp = [1 for i in range(x)]                             
                                                       
for i in range(x):                                    
    for j in range(i):                                 
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
            
#가장 긴 증가하는 부분 수열의 길이
print(dp)