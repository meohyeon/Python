#프로그래머스 숫자 짝궁
print("수로 이루어진 문자열 입력")
x = input()
y = input()
answer = ""
count = [0]*10

for i in range(9,-1,-1):
        count[i] = min(x.count(str(i)), y.count(str(i)))
        a=str(i)*count[i]
        if a != 0:
            answer += str(a)       
if sum(count)==0:
    answer = "-1"   
if (answer.count('0')==len(answer)):
    answer = "0"
print(answer)
