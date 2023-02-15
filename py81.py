# 프로그래머스 최소 직사각형 
test1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
test2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	
test3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
test = [test1,test2,test3]
for i in test:
    a = [min(x) for x in i]
    b = [max(x) for x in i]
    print(max(a)*max(b))