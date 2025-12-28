'''
BOJ 2579 - Stair Climbing
Category: Brute Force
Approach:
    - 전역 nonlocal 변수 
    - 종료 조건은 마지막 칸에 도착했을 때

Required: 총 점수의 최댓값 구하기
Result : Brute Force 시간 초과 
'''

import sys 

def solve():
    input = sys.stdin.readline
    N = int(input().strip())
    table = [0] + [int(input().strip()) for _ in range(N)]
    opt = 0 

    def dfs(pos, add, total):  # (현재 위치, 연속 계단 수, 총 점수 합)
        nonlocal opt   # nonlocal opt를 하는 이유는 지역변수로 하면 초기화되기 때문에 이를 방지하기 위해서이다.

        if pos == N:
            opt = max(opt, total)
            return
        
        # 1칸 올라갈 때 
        nxt = pos + 1
        if nxt <= N and add < 2:
            dfs(nxt, add + 1, total + table[nxt])

        # 2칸 올라갈 때 
        nxt = pos + 2
        if nxt <= N:
            dfs(nxt, 1, total + table[nxt])

    if N >= 1:
        dfs(1, 1,table[1])
    if N >= 2:
        dfs(2, 1, table[2]) 

    print(opt)

solve()