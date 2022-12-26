# 프로그래머스 짝지어 제거하기 level 2
s = input()
answer = 0
arr = []
if len(s) % 2 !=0:
    print(0)
for i in s:
    if len(arr) == 0:
        arr.append(i)
    else:
        if arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)
if len(arr) == 0:
    answer = 1
print(answer)