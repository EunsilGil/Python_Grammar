# 문자열 작성 예시
str1 = "Hello world"
str2 = 'Coding Campus'
str3 = """동해물과 백두산이 마르고 닳도록 
하느님이 보우하사 길이 보전하세 
무궁화 삼천리 화려강산"""

print(str1)
print(str2)
print(str3)

#<------- print 함수-------->
str1 = 'python'
int1 = 100
float1 = 95.2

# 변수를 그대로 출력
print(str1)
print(int1)
print(str1, int1)
print(int1 + float1) # print 함수 내에서의 연산이 가능하다.

# 변수를 새로운 문자열과 이어서 출력
# , +를 활용하여 문자열을 이어서 출력할 수 있다.
print("제가 가장 좋아하는 컴퓨터 언어는 ", str1, "입니다.")

# str 연산자를 활용하는 방법
print("제가 가장 좋아하는 컴퓨터 언어는 "+ str1+ "입니다.") 

# 문자열과 정수의 연산이 불가하므로 다음 식은 error가 된다.
# print("제 점수는 " + int1 + "점 입니다.") # error

# str format
print(f"저의 수학 점수는 {int1}점 입니다.")
print(f"""저는 {str1}시험에서 {float1}점을 받았지만, 
다음에는 {int1}점을 받을 것입니다.""")

#<------- input 함수-------->
# input 함수 사용 예시
school = input("학교를 입력하세요 : ")
print(school)

# 발 사이즈는 실수형 자료형이므로 int로 자료형 변환이 필요
# input함수의 매개변수가 없으므로, console에는 커서만 나타남
foot_size = int(input())
print(foot_size - 100)

#<------- 탈출문자-------->
# \n : 줄바꿈
print("안녕하세요. \n저는 파이썬을 좋아합니다.")   
# result : 안녕하세요.
#          저는 파이썬을 좋아합니다.

# \" : 큰 따옴표 출력
print("제가 가장 좋아하는 문장은 \"사랑합니다\"입니다.")  
# result : 제가 가장 좋아하는 문장은 "사랑합니다"입니다.
# 다음과 같이 큰 따옴표와 작은 따옴표를 표현할 수도 있다.
print("제가 가장 좋아하는 문장은 '사랑합니다'입니다.")
print('제가 가장 좋아하는 문장은 "사랑합니다"입니다.')   

# \\ : \(슬래시) 출력
print("C:\\Users\\Desktop")     # result : C:\Users\Desktop

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")        # result : PineApple

# \b : 한글자 삭제
print("Redd\b Apple")           # result : Red Apple

# \t : 탭 삽입
print("Red\tApple")             # result : Red    Apple

#<------- 문자열 추출(슬라이싱)-------->
# 문자열 추출(슬라이싱) 예시
str_slicing = '안녕하세요. 저는 ***입니다.'

print("첫번째 문자 추출 >>", str_slicing[0])

print("특정위치부터:특정위치까지 추출 >>", str_slicing[10:13])

# 문자열의 처음이 start 포인트이면 생략가능
print("처음부터:특정위치까지 추출 >>", str_slicing[:6])  

# 문자열의 마지막이 end 포인트이면 생략가능
print("특정위치부터:끝까지 추출 >>", str_slicing[7:])  

print("처음부터:끝까지:2칸씩 증가하며 추출 >>", str_slicing[::2])

print("처음부터:끝까지:-1칸씩 감소하며 추출 >>", str_slicing[::-1])

# 특정 인덱스 값을 가지고 오는 두 가지 방법
print("양수 사용 >>", str_slicing[7:9])
print("음수 사용 >>", str_slicing[-10:-8])

#<------- 문자열 처리 함수/메서드-------->
# 주요 문자열 처리 함수/메서드 사용 예시
num = '1 2 3 4 5 6 7 8 9 10'

print(num.count('1'))

print(num.find('0'))

str1 = 'abc'
str2 = 'DEFG'

print(str1.upper() + str2.lower())

print(num.replace('5 ', '5였던자리'))

print(','.join(str1))
print(str1.join(',,,,,,'))

print('a,b,c,d'.split(','))
print('hello world'.split()) # 공백을 기준으로 분할 

#<------- 예제 문제 -------->
# 전화번호를 입력받아 가장 마지막 4자리를 ****로 변환하는 프로그램

phone = input("핸드폰번호를 입력하세요 : ")
print(phone.replace(phone[-4:], '****'))

# 주민등록번호를 입력받아 '-'를 제외하여 출력하는 프로그램

id_num = input("주민등록번호를 입력하세요 : ")
print(id_num.replace('-', ''))

# 주민등록번호를 입력받아 
# 1. 태어난 년도
# 2. 생일
# 3. 성별
# 위의 3가지를 출력하는 프로그램

# 위에서 선언한 변수를 그대로 사용
year = id_num[:2]
birth = id_num[2:6]
gender = id_num[7]

print(f"당신이 태어난 년도는 {year}이고, 당신의 생일은 {birth}입니다. 당신의 주민등록번호 뒷자리는 {gender}로 시작합니다.")