# 프로그래머스 124 나라의 숫자 level2
n = int(input())
answer = ""
while n >= 1:
    if n % 3 == 0:
        answer = "4" + answer
        n = n//3 -1
    else:
        answer = str(n%3) + answer
        n = n//3
print(answer)