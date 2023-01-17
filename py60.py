# 프로그래머스 자연수 뒤집어 배열로 만들기
n = int(input())

answer = [int(x) for x in str(n)]
answer.reverse()
print(answer)