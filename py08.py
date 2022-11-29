#프로그래머스: 코딩테스트 연습 > 두 정수 사이의 합 
print("실수 2개 입력")
a, b = map(int, input().split())

total = 0

if a > b :
    a, b = b, a

total = sum(range(a,b+1))
print(total)

