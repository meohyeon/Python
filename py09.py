#프로그래머스: 코딩테스트 연습 > 삼총사
from itertools import combinations

print("수 입력")
n = list(map(int,input().split()))

total = 0

a = list(combinations(n,3))

for i in range(len(a)):
    if sum(a[i]) == 0:
        total += 1

print(total)