
s = input()
answer = 0
for i in range(len(s)):
    bol = True
    arr = []
    for j in s:
        if j == "[" or j == "(" or j == "{":
            arr.append(j)
        elif j == ']':
            if len(arr) == 0 or arr.pop() !="[":
                bol = False
                break
        elif j == ')':
            if len(arr) == 0 or arr.pop() !="(":
                bol = False
                break
        elif j == '}':
            if len(arr) == 0 or arr.pop() !="{":
                bol = False
                break
    if bol and len(arr) == 0:
        answer +=1
    s = s[1:] + s[0]
print(answer)