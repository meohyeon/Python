#프로그래머스 하샤드 수 
x = int(input())

n = sum([int(a) for a in str(x)])

if x % n == 0:
    answer = True
else:
    answer = False

print(answer)