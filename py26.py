#프로그래머스 튜플 level2
s = input()
answer = []
s = s[2:-2].split('},{')
s.sort(key=len)
for i in s:
    a = i.split(',')
    for i in a:
        if int(i) not in answer:
            answer.append(int(i))
print(answer)