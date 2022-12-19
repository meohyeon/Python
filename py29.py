# 프로그래머스 피보나치 수 level 2
n = int(input())
fibo = [0,1]
for i in range(2,n+1):
    fibo.append(fibo[i-1]+fibo[i-2])
answer = fibo[n] % 1234567

print(answer)