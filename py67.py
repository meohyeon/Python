#프로그래머스 정수 제곱근 판별
n = int(input())
if int(n**0.5) != n**0.5:
    answer = -1
else:       
    answer = ((n**0.5)+1)**2

print(int(answer))