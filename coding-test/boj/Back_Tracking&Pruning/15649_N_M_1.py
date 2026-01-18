'''
[문제 유형]
완전탐색(Brute Force) / 백트래킹 / 가지치기
[조건]
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

[결과 값]
길이가 M인 수열을 모두 구하여라.
'''

import sys
N, M = map(int, sys.stdin.readline().split())
# strip(제거할 문자들) : 앞과 뒤에서만 제거됨. 인자를 안 주면 -> 공백 문자 전체 제거 

visited = [False] * (N+1)
path = [] # path를 2차원으로 만들어야 할까?

def dfs(depth):
    if depth == M:  # depth는 N이 아니고 M이다.
        print(*path)    # * unpacking : 리스트의 값을 하나씩 풀어주는 역할 
        return 

    for i in range(1, N+1):
        if visited[i]:
            continue
        
        visited[i] = True # == 가 아니다
        path.append(i)

        dfs(depth + 1)

        # 백트래킹
        path.pop()
        visited[i] = False

dfs(0)