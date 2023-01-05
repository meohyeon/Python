#프로그래머스 이진 변환 반복하기 level 2
s = input()
zerocnt = 0
count = 0
while len(s) > 1:
    zerocnt += s.count('0')
    count += 1
    change = bin(s.count('1'))
    s = change[2:]
print([count,zerocnt])