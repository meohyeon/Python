#프로그래머스 숫자 문자열과 영단어 
n = input()
answer = ""
string = ""
list = ['zero','one','two','three','four','five','six','seven','eight','nine']
for i in n:
    if "0" <= i <= "9":
        answer += i
    else:
        string += i
        if string in list:
            answer += str(list.index(string))
            string =""
print(answer)

# replace 이용한 방법 

for i in range(len(list)):
    n = n.replace(list[i],str(i))
print(n)