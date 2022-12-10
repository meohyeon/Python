#프로그래머스 가장 가까운 같은 글자 
s = input()

answer = []
lis = {}
for i in range(len(s)):
    if not s[i] in lis:
        answer.append(-1)
            
    else:
        answer.append(i-lis[s[i]])
    lis[s[i]] = i
print(answer)