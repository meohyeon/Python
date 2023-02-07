#프로그래머스 약수의 개수와 덧셈
left, right = map(int,input().split())
answer = 0
for i in range(left,right+1):
    if int(i**0.5) == i**0.5:
        answer -= i 
    else:
        answer += i
print(answer)