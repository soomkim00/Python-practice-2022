# 문자열 입력 받음 > 내장 함수를 이용해서 유형 판별 > 각각 변수 0 초기화 += > 출력
# while True > EOFError try, except EOFError : break : 반복, 종료 조건
# import sys

import sys
lines = []
for line in sys.stdin:
    lines.append(line)


for i in lines:
    lo, up, num, sp = 0, 0, 0, 0
    for j in i:
        if j.islower():
            lo += 1
        elif j.isupper():
            up += 1
        elif j.isdigit():
            num += 1
        else:
            sp += 1
    if sp != 0:
        sp -= 1
    print(lo, up, num, sp)
