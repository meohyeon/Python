# 프로그래머스 최솟값 만들기 level 2
A = list(map(int,input().split()))
B = list(map(int,input().split()))

answer = 0

A.sort()
B.sort(reverse=True)

for i in range(len(A)):
    answer += A[i] * B[i]
# zip 함수 이용 방법 
#answer = sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
print(answer)