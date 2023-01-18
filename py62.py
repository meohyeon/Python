#프로그래머스 나누어 떨어지는 숫자 배열 
arr = list(map(int, input().split()))
divisor = int(input())
answer = sorted([x for x in arr if x%divisor == 0])
if not answer:
    answer =[-1]
print(answer)