#프로그래머스: 코딩테스트 연습 > 핸드폰 번호 가리기
print("전화번호 입력하세요")
phone_number=input()
answer = ''       
answer = '*'*(len(phone_number)-4) + phone_number[(len(phone_number)-4):]

print(answer)