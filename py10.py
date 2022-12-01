#프로그래머스: 코딩테스트 연습 > 두개 뽑아서 더하기 
from itertools import combinations

print("수 입력")
n = list(map(int,input().split()))
a = list(combinations(n, 2))

answer = []

for i in range(len(a)):
    answer.append(sum(a[i]))
answer = sorted(list(set(answer)))

print(answer)