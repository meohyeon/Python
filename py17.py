#프로그래머스 1부터 n까지 소수 찾기
n = int(input())
#에라토스테네스의 체 활용
list = set(range(2,n+1))
for i in range(2,n+1):
    if i in list:
        list -=  set(range(2*i,n+1,i))

print(list)