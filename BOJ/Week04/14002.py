x = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
            
max_dp = max(dp)  #가장 긴 증가하는 부분 수열의 길이
print(max_dp)
max_idx = dp.index(max_dp) #max_dp의 위치
lis = []  #가장 긴 증가하는 수열을 담을 list
while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(arr[max_idx])
        max_dp -= 1 #가장 큰 값을 뺐으니 길이를 하나 줄여서 
        print(lis)
        
    max_idx -= 1   #가장 큰 값부터 역순으로 찾아간다. 
    # 이게 가능한 이유는 어차피 dp에 모든 최대 수열 길이가 저장되어 있기때문에
    # 하나씩 줄여나가면 자연스레 직전 수열로 오게될 수 밖에 없다. 그리고 최대 부분 수열중에서도 아무거나 출력하면 
    # 되기 때문에 상관없는것. 
    
lis.reverse()
print(*lis)
print(dp)