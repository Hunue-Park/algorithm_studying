# finding parents of Tree

import sys
input = sys.stdin.readline

# 이 함수는 인터프리터의 스택제한을 설정하는 것이기 때문에 pypy 사용시 메모리 초과난다. -> 이사람 제정신아님. 
# 재귀함수 호출 depth 가 아닌 인터프리터의 스택제한을 설정하는 것이다. 
sys.setrecursionlimit(10**5)

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, tree, parents)

if __name__ == "__main__":
    N = int(input())
    Tree = [[] for _ in range(N+1)]
    Parents = [0 for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        Tree[a].append(b)
        Tree[b].append(a)

    

    DFS(1, Tree, Parents)
    for i in range(2, N+1):
        print(Parents[i])