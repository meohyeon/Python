#프로그래머스 기능개발 level 2
import math
from collections import deque

progresses = list(map(int,input().split()))
speeds = list(map(int,input().split()))

answer = []
q = deque()
count = 0

for i in range(len(progresses)):
    q.append(math.ceil((100 - progresses[i]) / speeds[i]))

while q:
    index = q.popleft()
    count = 1
    while q:
        if index < q[0]:
            break
        else:
            count += 1
            q.popleft()
    answer.append(count)

print(answer)