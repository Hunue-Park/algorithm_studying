# multi taps
# 집이넣는 전기용품 기준으로 이후의 순번에서 가장 나중에 있는 이미 꼽혀있는 번호를
# 뽑고, 해당 전기용품을 꼽는다. 

from sys import stdin
N, K = stdin.readline().split()
N = int(N)
K = int(K)
multap = [0] * N
li = list(map(int, stdin.readline().split()))
res = swap = num = max_I = 0
for i in li:
    if i in multap:
        pass
    elif 0 in multap:
        multap[multap.index(0)] = i
    else:
        for j in multap:
            if j not in li[num:]:
                swap = j
                break
            elif li[num:].index(j) > max_I:
                max_I = li[num:].index(j)
                # 위에서 인덱스를 확인하되 해당 인덱스에 해당하는 값
                # 인덱스로 concent에서 바꾸는게 아니라 정확히 매칭되는 값으로 
                # 값 대 값으로 바꿔야 list index 에러가 안난다. 
                swap = j
        multap[multap.index(swap)] = i
        max_I = swap = 0
        res += 1
    # 이 num 은 li 의 시작 인덱스 조절용.
    num += 1
print(res)