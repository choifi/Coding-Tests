'''
[풀이 방법]
DP : 각 항목마다 memo하며 '가장 긴 감소하는 부분 수열'의 '길이' 출력

수열 : 수를 어떤 규칙에 따라 순서대로 나열한 것
부분 수열 : 주어진 수열에서 일부 원소를 원래 순서대로 그대로 뽑아 만든 새로운 수열. 전체 수열도 포함.
'''

import sys
N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split(' ')))
memo = [1] * N # memo[i]의 상태는 "list[i]번째 값이 부분 수열의 최댓값인 길이의 최댓값"
# 길이의 최솟값은 1이다.

for i in range(0,N):
    for j in range(0,i):
        if list[j] > list[i]:
            memo[i] = max(memo[i], memo[j]+1)

# [10,30,10,20,20,10]

#1 1 1 1 1 1 
#    2 1 1 1 
#    2 2 1 1
#1 1 2 2 2 1
#1 1 2 2 2 3
          
print(max(memo))
# 왜 틀렸을까?
# 문제 풀 때는 반증을 생각해야 합니다.


