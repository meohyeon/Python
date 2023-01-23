# 프로그래머스 문자열 내림차순으로 배치
s = input()
answer = sorted(s,reverse=True)
print("".join(answer))