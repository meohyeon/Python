# 프로그래머스 문자열 내 p와 y의 개수 
s = input()

answer = True
a = s.lower().count("p")
b = s.lower().count("y")
if a != b:
    answer = False
print(answer)