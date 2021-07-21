# 자료구조의 변경
menu = {"커피", "우유", "주스"} # set
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


###############################################
# 예제문제

# 1명은 치킨, 3명은 커피쿠폰을 주는 추첨 프로그램
# 조건 1 : 댓글 작성자는 20명, ID는 1~20
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨, 중복 불가
# 조건 3 : random 모듈의 shuffle, sample 활용

from random import *

person_id = range(1, 21)
person_id = list(person_id)

shuffle(person_id)
# print(person_id)

당첨자 = sample(person_id, 4) # 4명의 당첨자를 추첨

print(당첨자)
print ('---당청자 발표---')
print('치킨 당첨자 : ', 당첨자[:1])
print('커피 당첨자 : ', 당첨자[1:])
print('--- 축하합니다 ---')

# print('치킨 당첨자 : {0}' .format(당첨자[0]))
# print('커피 당첨자 : {0}' .format(당첨자[1:]))