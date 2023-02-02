# 프로그래머스 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
star  = ('*'*a+"\n")*b
print(star)