s = input()
answer = False
arr = []    
for i in s:
    if i == '(':
        arr.append(i)
    elif i == ')':
        if len(arr) > 0:
            arr[-1] == '('
            arr.pop()
        else:
            arr.append(i)
if len(arr) == 0:
    answer = True
print(answer)