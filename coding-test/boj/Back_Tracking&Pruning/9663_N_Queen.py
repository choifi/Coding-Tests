'''
[ 유형 ]
BackTracking & 가지치기
[ 가지치기 핵심 ] 
행/열/대각선(우상향,좌하향) 충돌하면 바로 컷하기 
[ 문제 ]
크기가 N x N인 체스판 위에 '퀸 N개'를 서로 공격할 수 없게 놓는 문제 

[ 기타 ]
row: 행(가로), col: 열(세로), diagonal: 대각선
'''

import sys
input = sys.stdin.readline

# TODO A: 입력 받기
N = int(input().strip())

# TODO B: 충돌 체크 배열 준비 
# col[c] = True이면 c열에 이미 퀸이 있음
col = [False] * N
# diag1[d] = True이면 (r+c)가 같은 대각선에 이미 퀸이 있음 (0 ~ 2N-2)
diag1 = [False] * (2*N-1)
# diag2[d] = True이면 (r-c+N-1)가 같은 대각선에 이미 퀸이 있음 (0 ~ 2N-2)
diag2 = [False] * (2*N-1)

# TODO C: 정답 카운트
count = 0
# TODO D: DFS 정의
def dfs(r): # r번째 행에 퀸을 놓는 과정
    global count
    # D-1: 종료 조건 (N개 다 놓았으면 1가지 완성)
    if r == N:
        # 경우의 수 출력 
        count += 1
        return
    
    # D-2: 현재 행 r에서 열을 하나 선택 
    for c in range(0, N):
        # D-3: 가지치기 (불가능 판정)
        # - 같은 열 이미 사용 
        # - 같은 대각선 이미 사용 
        if col[c] == True or diag1[r+c] == True or diag2[r-c+N-1] == True:
            continue
        
        # D-4: 선택 (퀸 배치)
        col[c] = True
        diag1[r+c] = True
        diag2[r-c+N-1] = True
 
        # D-5: 다음 행으로 
        dfs(r + 1)

        # D-6: 되돌리기(백트래킹)
        col[c] = False
        diag1[r+c] = False
        diag2[r-c+N-1] = False

# TODO E: DFS 시작
dfs(0)

# TODO F: 출력 
print(count)