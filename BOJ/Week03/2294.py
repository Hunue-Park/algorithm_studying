# coins 2
from collections import deque
import sys
input = sys.stdin.readline

def cal_coins(coin_list):
    visited = [0] * 10001
    min_count = 10001
    while q:
        cur_coin, count = q.popleft()
        for i in range(N):
            new_coin = cur_coin + coin_list[i]
            if new_coin > K:
                break
            # 요 테크닉이 이미 만들어진 코인값을 체크해줌 
            if visited[new_coin] == 1:
                continue
            if new_coin < K and count + 1 < min_count:
                visited[new_coin] = 1
                q.append((new_coin, count + 1))
            elif new_coin == K:
                min_count = min(min_count, count + 1)

    if min_count == 10001:
        min_count = -1
    print(min_count)

if __name__ == "__main__":
    N, K = map(int, input().split())
    coin_list = []
    for _ in range(N):
        coin_list.append(int(input().strip()))

    coin_list.sort()
    q = deque() 
    for coin in coin_list:
        q.append((coin, 1))
    cal_coins(coin_list)