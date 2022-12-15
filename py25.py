# 프로그래머스 n queen level 2

n = int(input())

def solution(n):
    lis = [0] * (n+1)
    return recol(0,n,lis)
def recol(a,n,lis):
    answer = 0
    if a == n:   
        return 1
    else:
        for i in range(n):
            lis[a] = i
            if check(a,lis):
                answer += recol(a+1,n,lis)
    return answer
def check(a,lis):
    for i in range(a):
        if lis[a] == lis[i] or (a-i == abs(lis[a]-lis[i])):
            return False
    return True
print(solution(n))