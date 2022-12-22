# 프로그래머스 다음 큰 숫자 level2
n = int(input())

answer = 0
cnt = bin(n).count('1')
for i in range(n+1,n**2+1,1):
    if bin(i).count('1') == cnt:
        answer = i 
        break
print(answer)
    