''''
BOJ 1463 - Make One
Category: Dynamic Programming
Approach: Bottom-up DP

# 이게 왜 DP인가?
- 연산을 사용해서 1로 만드는 최솟값을 구해야 한다. 
-> memoization을 사용해서 횟수를 기록해야 한다. [중복 계산을 제거하여 같은 계산을 다시 하지 않도록 한다.]

# 왜 Bottom-up인가?
구해야하는 수 1이 이미 지정되어있다 -> 연산을 해서 정수 X를 구하면 된다

# 저장할 단위 state
해당 연산 횟수를 기록한다.
'''

import sys
input = int(sys.stdin.readline())

X = input
memo = [0] * (X+1) # 인덱스랑 정수랑 일치시킨다.

# bottom-up
for i in range(2, X+1):  # i는 2부터 X까지
    memo[i] = memo[i-1] + 1
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3]+1)
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2]+1)

print(memo[X])



