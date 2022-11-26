#프로그래머스: 코딩테스트 연습 > 약수의 합
import math
print("정수 n 입력")
n=int(input())
answer = 0
a = []

for i in range(1, n+1):
    if(n%i==0):
        a.append(i)

answer=sum(a)
print("약수의 합: "+str(answer))
    
        
