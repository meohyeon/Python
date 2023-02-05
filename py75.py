# 프로그래머스 내적
a = list(map(int,input().split()))
b = list(map(int,input().split()))
answer = [x*y for x,y in zip(a,b)]
print(sum(answer))