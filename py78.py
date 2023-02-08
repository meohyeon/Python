#프로그래머스 크기가 작은 부분문자열
t = input()
p = input()
answer = 0
for i in range(len(t)-len(p)+1):
    if int(t[i:i+len(p)]) <= int(p):
        answer +=1
print(answer)