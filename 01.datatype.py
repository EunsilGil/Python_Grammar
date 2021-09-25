# 변수 
# data type 을 저장할 수 있습니다.
# 숫자 : 정수 자료형(int), 실수 자료형(float))
# 문자열 자료형(str)
# boolean : 참과 거짓을 나타내는 자료형 (bool)
# list, dictionary
int1 = 10
int2 = -10
float1 = 9.9999
float2 = -9.9999
str1 = "python"
str2 = 'hello'
bool1 = int1 >= 3 # true or false

# print 사용법
# 1. 변수를 그대로 출력
print (str2)
# 2. 변수와 문자열을 이어서 출력하는 방법
print ('제 동생의 나이는', int1,"살 입니다.")

# 변수의 데이터 타입에 따라서 가능한 연산이 제한됩니다.
print ('제 동생의 나이는 ' + str(int1) + "살 입니다.")

# 문자열 format
print(f"제 동생은 {int1}살 입니다.")
print(f'제가 가장 좋아하는 컴퓨터 언어는 {str1}이고, 저는 {str1}을 {int1}개월 배웠습니다.')

######################################################

# 산술연산자
# 피연산자가 무엇인지에 따라 연산자의 용도가 달라집니다.
print(2 + 3)  # 5
print(2 - 3)  # -1
print(2 * 3)  # 6
#제곱
print(2 ** 3) # 8
# 나눗셈 : 나눗셈 계산을 하면 결과가 늘 float(실수 자료형)으로 반환됩니다.
print(3 / 2)  # 1.5
print(4 / 2)  # 2.0
# 몫
print(3 // 2) # 1
# 나머지
print(3 % 2)  # 1

# 연산자를 이용해서 문자열의 연산도 가능합니다.
print('hello' * 5) # hello hello hello hello hello
print("l love" + "python") # l lovepython
# print("안녕하세요" - "하세요") # error
# print("내 수학점수는 " + 0 ) # error
# print('aaaaaa' / 6) # error 

# 논리 연산자
print(10 > 3) #t
print(4 >= 7) #f
print(10 < 3) #f
print(5 <= 5) #t
print(3 == 3) #t
# ~가 아니다
print(3 != 3) #f

# not : 현재 상태에 대한 부정 : t > f, f > t
print(not(1 != 3))  #f
# and : 곱셈연산과 비슷하다 : t and t일 경우에만 t
print((3 > 0) and (3 < 5))  #t
print((3 > 0) & (3 < 5))   #t
# or : 덧셈연산과 비슷하다 : f or f일 경우에만 f
print((3 < 0) or (3 < 5)) #t 
print((3 > 0) | (3 < 5))  #t

# and연산
print (5 > 4 > 3) #t
print (5 > 4 > 7) #f

################################################

# 문자열
# ""(큰 따옴표), ''(작은 따옴표)를 이용해서 문자열을 작성할 수 있다.
# 문자열에 enter(줄바꿈)을 포함할 수 있다.
str3 = """
-나는 천재다.
그리고, 바보다.-
        몰라
"""
print(str3)

# 슬라이싱 : 문자열 추출하기

주민등록번호 = '081205-3011111'

# index를 이용하여 문자열을 추출할 수 있습니다.
# index는 0번째부터 시작합니다.
print("성별 :" , 주민등록번호[7])
print("태어난 년도 :", 주민등록번호[0:2]) # 0번째부터 2번째 직전까지 >> 0번째부터 1번째까지
print("생일 :", 주민등록번호[2:6])
print("생년월일 :", 주민등록번호[:6]) # 처음부터 6번째 직전까지 >> 0은 생략이 가능합니다.
print("뒤 7자리 :", 주민등록번호[-7:]) # 뒤에서부터 순차적으로 문자열을 추출할 수도 있습니다.

# 문자열 처리 함수
python = 'Python is Amazing'

# 문자열 길이
print(len(python))
# 소문자로 출력
print(python.lower())
# 대문자로 출력
print(python.upper())
# 문자열에서 원하는 문자 찾기
print(python.find('n'))
print(python.find("is")) # 찾고자하는 문자열이 가장 먼저 등장하는 곳의 index를 반환
print(python.find("java")) #원하는 값이 없으면 -1을 return
# 문자열에서 해당 문자가 몇번 등장하는지 count
print(python.count('n'))

# 탈출 문자 : \와 함께 사용
# \n : 줄바꿈
print("백문이 불여일견 \n  백견이 불여일타")

# 큰따옴표 또는 작은 따옴표를 출력
print("저는 \"나도코딩\"입니다.")
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
# \ 를 출력
print("C:\\Users\\Desktop")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 한글자 삭제 (backspace)
print("Redd\b Apple")
# \t : tab
print("Red \t Apple")