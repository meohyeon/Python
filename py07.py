#프로그래머스: 코딩테스트 연습 > 없는 숫자 더하기
# 0 <= numbers원소 <=9

numbers = list(map(int, input()))
total = 0
print(numbers)
for i in range(1,10):
    if i not in numbers:
        total += i
print(total)

# 다른 방법
total2 = [x for x in range(10) if x not in numbers]
print(sum(total2))