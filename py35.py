# 프로그래머스 jadencase 문자열 만들기 level 2
s = input()
arr = s.split(" ") #공백문자가 연속해서 나올 경우 대비하여 한번씩만 제거 
answer = ''

for i in arr:
    a = ''
    for j in range(len(i)):
        if j == 0:
            if 97<= ord(i[j]) <=122:
                a += i[j].upper()
            else:
                a += i[j]
        else:   
            a += i[j].lower()
    answer += a +" "
answer = answer[:-1]

print(answer)

#타이틀 함수 : 문자열 앞만 대문자로 
#print(s.title())