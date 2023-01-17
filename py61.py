# 프로그래머스 음양 더하기
absolutes = [4,7,12]
signs = [True,False,True]

answer = [x if bol else -x for x, bol in zip(absolutes,signs)]
print(sum(answer))