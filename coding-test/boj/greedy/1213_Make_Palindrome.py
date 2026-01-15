''' 
[정의]
Palindrome(팰린드롬) : 앞으로 읽으나 뒤로 읽으나 동일한 단어, 문장, 숫자, 문자열 등

[문제 유형]
Greedy - 그때 그때 선택을 하기 때문이다. 즉시 확정

[문제 풀이]
- 문자열을 오름차순 정렬한다. 
- 각 문자열을 개수를 샌다. 딕셔너리로 만든다 ?   

- leftover는 (각 문자열의 개수 % 2)의 합이다.
  leftover == 0이면 팰린드롬를 만든다
  leftover == 1이면 그 수를 중앙에 위치시킨 팰린드롬을 만든다.
  leftover > 1이면 "I'm Sorry Hansoo."를 출력하고 종료한다.

[결과]
- 정답이 여러개 일때는 사전적으로 앞서는 것을 출력한다.
'''

import sys
N = list(map(str, sys.stdin.readline().strip())) # strip()을 하지 않으면 /n이 들어감
N.sort() # 기존의 리스트를 수정하여 정렬된 결과를 반환
dict_N = {} # 각 문자열의 개수 count 
for i in N:
    if i not in dict_N.keys():
        dict_N[i] = 1
    else:
        dict_N[i] += 1

leftover = 0
half_result = ''
solo = ''
isResult =  True
for key, value in dict_N.items(): # leftover가 1 초과일 경우는 문자열 출력
    leftover += value % 2
    if leftover > 1:
        print("I'm Sorry Hansoo")
        sys.exit()
    if value % 2 == 0:
        half_result += key * (value//2)
    if value % 2 == 1:
        half_result += key * (value//2)
        solo = key

result = half_result + solo + half_result[::-1]

print(result)



