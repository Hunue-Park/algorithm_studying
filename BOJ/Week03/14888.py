# inserting operators. 

import sys
input = sys.stdin.readline

def DFS(cur_value, next, ops_idx):
    if next > N-1 or ops_counting[ops_idx] == 0:
        return
    if ops_idx == 0 and ops_counting[0] != 0:
        cur_value = cur_value + nums[next]
        ops_counting[0] -= 1
    elif ops_idx == 1 and ops_counting[1] != 0:
        cur_value = cur_value - nums[next]
        ops_counting[1] -= 1
    elif ops_idx == 2 and ops_counting[2] != 0:
        cur_value = cur_value * nums[next]
        ops_counting[2] -= 1
    elif ops_idx == 3 and ops_counting[3] != 0:
        cur_value = cur_value // nums[next]
        ops_counting[3] -= 1
    for i in range(4):
        DFS(cur_value, next + 1, i)

    cal_list.append(cur_value)
    return cur_value

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    N = int(input())
    nums = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    cal_list = []
    for i in range(4):
        ops_counting = [operators[0], operators[1], operators[2], operators[3]]
        DFS(nums[0], 1, i)

    print(cal_list)

######### 정답코드와 비교 
# 우선 재귀 함수 변수에 연산자 개수를 넣는 방법이 아주 참신하다. 
# 나머지는 대부분 동일. 
# 아 그리고 global maxv 선언해서 dfs 내부에서 가능한 reaf node 에 도달햇을때 계속해서 갱신.