#프로그래머스: 코딩테스트 연습 >  문자열 대소문자 변경
n = input()

answer = []
a = list(n.split(" "))

for i in a:
    b=""
    for j in range(len(i)):
        if j % 2 == 0:
            b += i[j].upper()
        else:
            b += i[j].lower()
    answer.append(b)

print(' '.join(answer))
