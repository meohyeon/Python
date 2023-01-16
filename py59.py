# 프로그래머스 카펫 level 2
brown = int(input())
yellow = int(input())

#yellow 가로+세로 == brown - 꼭지점 // 2 
n = (brown-4)//2

#곱했을떄 yellow 넓이와 같은 가로 세로 길이 구함 조건: 가로 >= 세로
for i in range(n):
    x, y = n-i, i
    if x*y == yellow:
        print(x+2,y+2)
        break