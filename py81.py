# 프로그래머스 최소 직사각형 
test = [[60, 50], [30, 70], [60, 30], [80, 40]]
a = [min(x) for x in test]
b = [max(x) for x in test]
print(max(a)*max(b))
