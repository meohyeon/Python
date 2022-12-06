# 프로그래머스 부족한 금액 계산 
price, money, count = map(int, input().split())

total = 0
answer = 0
for i in range(count):
    total += (price*(i+1))

if total <= money:
    answer = 0
else:
    answer = total - money

print(answer)
    