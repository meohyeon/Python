#프로그래머스 나머지가 1인 수 찾기
n=int(input())
anwer=0

def asd(n):
    for i in range(1, n):
        if(n%i==1):
            return i   
anwer=asd(n)

print(anwer)