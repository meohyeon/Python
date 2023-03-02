#프로그래머스 뒤에 있는 큰 수 찾기 level2
numbers = list(map(int,input().split()))
answer = []
stack = []
answer = [0] * len(numbers)

for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
while stack:
        answer[stack.pop()] = -1

print(answer)