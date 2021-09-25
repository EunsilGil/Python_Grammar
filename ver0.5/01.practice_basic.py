# print 사용

animal = "고양이"
name = "시나브로"
age = 2
hobby = "산책"
is_adult = age >= 3
print ("우리집 " + animal + "의 이름은 " + name +"예요")
print (name +"는 " + str(4) + "살이며, " + hobby + "을 아주 좋아해요")
print (name, "는 어른일까요? ", is_adult)


#################################################################

# 연산자

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 ** 3)
print(2 / 3)
print(2 // 3) #몫
print(2 % 3) #나머지

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)
print(3 == 3)
print(3 != 3)

print(not(1 != 3))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 < 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print (5 > 4 > 3) #True
print (5 > 4 > 7) #False

###########################################################

# 숫자 처리 함수

print(abs(-5)) #절댓값
print(pow(4, 2)) # 4^2 = 16
print(max(5, 13))
print(min(5, 13))
print(round(3.14)) #반올림
print(round(3.7))

from math import *

print(floor(4.9)) #내림 = 4
print(ceil(3.1)) #올림 = 4
print(sqrt(16)) # 제곱근 = 4

###########################################################

# random 함수

from random import *

print(random()) # 0.0~1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 1~10 미만의 임의의 값을 정수로 변환
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45 + 1)) # 1 ~ 45 미만의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 

print("오프라인 스터디 모임 날짜는 매월 ", randint(4, 28), "일로 선정되었습니다.")