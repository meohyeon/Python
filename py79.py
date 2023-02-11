#프로그래머스 3진법 뒤집기
n = int(input())
answer = ""
while n >=1:
    n, m = divmod(n,3)
    answer += str(m)
print(int(answer,3))