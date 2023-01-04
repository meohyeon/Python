#프로그래머스 하노이 탑 level 2
n = int(input())
answer = []
def top(a,b,n):
    if n == 1:
        answer.append([a,b])
        return
    top(a,6-a-b,n-1)
    answer.append([a,b])
    top(6-a-b,b,n-1)
top(1,3,n)
print(answer)