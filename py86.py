#프로그래머스 주식 가격 level2
from collections import deque
prices = list(map(int,input().split()))
q = deque(prices)
answer = []
while q:
    value = q.popleft()
    cnt = 0
    for i in q:
        cnt += 1
        if value > i:
            break
    answer.append(cnt)
print(answer)