'''
[문제 유형]

[조건]
중복 없이 M개를 고른 수열
고른 수열은 오름차순

[ N과 M(1) 문제와 다른 점 ]
고른 수열은 오름차순 처리 [start]를 해 줌. start는 "오름차순 조건 + 중복 제거"를 담당한다. 따라서 visited가 필요없다. 
'''

import sys 
N, M = map(int, sys.stdin.readline().split())
path = []
# start는 다음에 뽑을 수 있는 최소 숫자. 

def dfs(depth, start): # depth는 지금까지 뽑은 개수 
    # 종료 조건
    if depth == M:
        print(*path)
        return
    
    # 선택 루프 (오름차순 + 사전순)
    for x in range(start, N+1):
        # 선택
        path.append(x)

        # 다음 단계 
        dfs(depth + 1, x + 1) # 다음 숫자는 반드시 더 커야 하므로 x+1부터 시작합니다. 

        # 되돌리기 - backtracking
        path.pop()

# DFS 시작
dfs(0,1)