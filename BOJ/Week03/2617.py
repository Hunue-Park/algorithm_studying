import sys
input = sys.stdin.readline


def DFS(node, list):
    global visited
    global check
    visited[node] = 1
    for bead in list[node]:
        if visited[bead] == 0:
            # 깊이 들어갈때마다 하나씩 카운트 업
            # 나보다 크다는 의미 이므로 
            check += 1
            DFS(bead, list)


if __name__ == "__main__":
    N, M = map(int, input().split())
    more_heavy = [[] for _ in range(N+1)]
    more_light = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        more_heavy[b].append(a)
        more_light[a].append(b)
    
    count = 0
    md = (N + 1) / 2
    for i in range(1, N+1):
        visited = [0] * (N+1)
        check = 0
        DFS(i, more_heavy)
        if check >= md:
            count += 1
        check = 0
        DFS(i, more_light)
        if check >= md:
            count += 1

    print(count)
