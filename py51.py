# 프로그래머스 큰 수 만들기 level 2
number = input()
k = int(input())
answer = []
for i in number:
    while answer:
        if answer[-1] < i and k > 0:
            answer.pop()
            k-=1
        else:
            break
    answer.append(i)
    

if k > 0:
    answer = answer[:-k]

print("".join(answer))