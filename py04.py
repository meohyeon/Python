#프로그래머스: 코딩테스트 연습 > 최대공약수와 최소공배수
import math
print("정수 두개 입력")
a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = math.lcm(a, b)

print("최대공약수 : " +str(gcd)+ " 최소공배수 : " + str(lcm))
