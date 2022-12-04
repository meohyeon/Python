# 프로그래머스 문자열 나누기 
print("문자열 입력")
n = input()
first = "zero"
answer = 0
count = [0,0]

for i in n:
    if first == "zero":
        first = i
    if i == first:
        count[0] += 1
    else:
        count[1] += 1
    if count[0] == count[1]:
        answer += 1
        first = "zero"
        count[0] = 0
        count[1] = 0
if first != "zero":
    answer += 1
print("총 문자열 갯수: " + str(answer))
