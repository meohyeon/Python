#프로그래머스: 코딩테스트 연습 > 소수 만들기  
from itertools import combinations
print("수 입력") # ex 1 2 3 4
n = list(map(int,input().split()))
answer = 0
    
a=([sum(a) for a in combinations(n,3)])
for i in a:
    count = 0      
    for j in range(2,i): 
        if i % j ==0:
            count +=1
    if count ==0:
        answer+=1 

print(answer)