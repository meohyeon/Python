# 프로그래머스 구명보트 level 2
from collections import deque
people = list(map(int, input().split()))
limit = int(input())

q = deque(sorted(people))
answer = 0
while len(q) > 1:
    if q[0] + q[-1] <= limit:
        answer += 1
        q.pop()
        q.popleft()
    else:
        answer += 1
        q.pop()

if q:
    answer +=1
print(answer)