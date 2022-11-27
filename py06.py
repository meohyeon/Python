#프로그래머스: 코딩테스트 연습 > 짝수의 합 
print("정수 입력")
n = int(input())
total = sum([i for i in range(2, n+1, 2)])

print("n까지 의 짝수의 합"+str(total))

