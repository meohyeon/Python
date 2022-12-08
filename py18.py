#프로그래머스 시저암호
s = input()
n = int(input())
answer =""

for i in s:
    count = ord(i)
    if 65 <= ord(i) <= 90:   
        for j in range(0,n):
            count += 1
            if count > 90:
                count -= 26
        answer += chr(count)         
    elif 90 < ord(i) <= 122:
        for j in range(0,n):
            count += 1
            if count > 122:
                count -= 26
        answer += chr(count)
    else:
        answer += " "
print(answer)