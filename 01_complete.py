print("제 이름은 *** 입니다")

# 변수 선언
int1 = 10
int2 = -10
float1 = 9.9999
float2 = -9.9999
str1 = "python"
str2 = 'hello'
bool1 = int1 >= 3 

#<------- 산술 연산자-------->
print(2 + 3)  # result : 5
print(2 - 3)  # result : -1
print(2 * 3)  # result : 6
# 제곱
print(2 ** 3) # result : 8
# 나눗셈 : 결과가 늘 소숫점이 있는 실수(float)로 반환
print(3 / 2)  # result : 1.5
print(4 / 2)  # result : 2.0
# 몫
print(5 // 3) # result : 1
# 나머지
print(5 % 3)  # result : 2

# 연산자를 이용해서 문자열의 연산도 가능
# But, 모든 연산이 가능한 것은 아니다.
# 아래 구문들 중 error가 발생하는 식도 있으므로, 추후에 꼭 주석처리를 해줘야한다.
print('hello' * 2)          # result : hellohello
print("l love " + "python") # result : I love python
# print("안녕하세요" - "하세요")  # result : error
# print("내 수학점수는 " + 0 )   # result : error
# print('aaaaaa' / 6)           # result : error

#<------- 비교 연산자-------->
print(10 > 3) # result : True
print(4 >= 7) # result : False
print(10 < 3) # result : False
print(5 <= 5) # result : True
# ~이다.
print(3 == 3) # result : True
print(3 == 5) # result : False
# ~가 아니다.
print(3 != 3) # result : False
print(3 != 5) # result : True

#<------- 논리 연산자-------->
# and >> 둘 다 참이어야 참, 나머지는 다 거짓
# and ==>  * 개념 >> 1(T) * 0(F)  = 0 
# or ==> + 개념 >> 1(T) + 0(F) = 1
print((3 > 2) and True)       # T and T >> True
print((3 == 3) and (3 != 3))  # T and F >> False 
print((3 != 3) & (4 != 4))    # F and F >> False
# or >> 둘 중 하나라도 참이면 참, 둘 다 거짓이어야 거짓
print((3 < 2) or True)        # F or T >> True
print((3 == 3) or (3 != 3))   # T or F >> True
print((3 != 3) | (4 != 4))    # F or F >> False
# not >> 현재의 부정
print(not(3 >= 2))    # not(T) >> False
print(not(3 != 3))    # not(F) >> True 

# and연산
print (5 > 4 > 3)     # result : True
print (5 > 4 > 7)     # result : False

#<------- 예제 문제-------->
# 입력받은 a와 b를 덧셈한 결과와, 그 결과가 10보다 큰지 작은지를 출력하는 프로그램

a = int(input("숫자를 입력하시오(a) >> "))
b = int(input("숫자를 입력하시오(b) >> "))

# @@@@@@ 를 채우세요.
print(a,"와", b,"를 더한 결과는", a+b, "입니다.")
print("덧셈의 결과가 10보다 큰가요? :", (a+b)>10 )