# 프로그래머스 정수 내림차순으로 배치하기
n = input()
answer = int("".join(sorted(str(n),reverse=True)))
print(answer)