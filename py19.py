#프로그래머스 > 예산 
from itertools import combinations
n = list(map(int, input()))
budget = int(input())

answer = 0
count = 0
n.sort()
for i in n:
    if (count + i ) <=budget:
        count += i
        answer += 1
    else:
        break
print(answer)
