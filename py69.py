#프로그래머스 가운데 글자 가져오기
s = input()
a = len(s)//2
if len(s) % 2 == 0:
    answer = s[a-1:a+1]
else:
    answer = s[a]
print(answer)