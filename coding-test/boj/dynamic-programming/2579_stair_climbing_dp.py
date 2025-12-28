'''
BOJ 2579 - Stair Climbing
Category: Dynamic Programming
Approach: Top-Down
- Top-Down은 "전체 상태 공간"을 채우려는 것이 아니라, "정답을 구성하는 데 실제로 필요한 상태만" 호출합니다.
- 정답을 만들기 위한 하위 문제를 요청합니다. 
'''

import sys 
input = int(sys.stdin.readline())

def solve():   # 총 점수의 최댓값 구하기
    N = input.strip()
    table = [0] + [input.strip() for _ in range(N)]
    dp = [-1 for _ in range(N+1)]

    def fib(n):
        if n <= 1:   # fib 정의, fib(0) = 0, fib(1) = 1
            return table[n]
    
        if dp[n] != -1:  # dp[n]에 값이 저장되어 있으면, 그 값을 바로 반환 [중복 계산 방지]
            return dp[n]
        
        # 최댓값(2칸 올라갔을 때, 1칸 올라갔을 때)를 구해준다. 
        fib(n) = max(fib(n-2) + table[n], fib(n-1) + table[n])

        # 3번 연속해서 올라갔을 때는 어떻게 해결할까? 

    fib(N)

solve()