#프로그래머스 제일 작은수 제거하기 

n = list(map(int, input().split()))
answer = 0

if len(n) == 1:
    answer.append(-1)
else:
    n.remove(min(n))
    answer = n

print(answer)