#프로그래머스 콜라츠 추측
num = int(input())
answer = 0
while num > 1:
    if num %2 == 0:
        num = num//2
        answer +=1
    else:
        num = num*3 +1 
        answer +=1
    if answer >= 500:
        answer = -1
        break 
print(answer)