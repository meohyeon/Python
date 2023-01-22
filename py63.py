# 프로그래머스 문자열 다루기
s = input()
answer = True
if len(s) == 4 or len(s) == 6:   
    for x in s:
        if ord(x) >=65:
            answer=False
else:
    answer = False
print(answer)