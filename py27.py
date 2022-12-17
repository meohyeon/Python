#프로그래머스 숫자의 표현 level 2 
n = int(input())

answer = 0
for i in range(1,n+1):
    total = 0
    for j in range(i,n+1):
        total += j
        if total == n:
            answer += 1
            break
        elif total > n:
            break
print(answer)