'''
[문제 유형]

[조건]
중복 없이 M개를 고른 수열
고른 수열은 오름차순
'''

import sys 
N, M = map(int, sys.stdin.readline().split())

visited = [False] * (N+1)
path = []
cur = 0

def dfs(depth):
    global cur
    if depth == M:
        print(*path)
        cur = 0
        return
    
    for i in range(1, N+1):
        if visited[i] or cur >= i:
            continue

        visited[i] = True
        path.append(i)
        cur = i

        dfs(depth + 1)

        # backtracking
        path.pop()
        visited[i] = False

dfs(0)