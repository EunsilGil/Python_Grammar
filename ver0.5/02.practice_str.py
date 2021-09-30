# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


#############################################################

# 슬라이싱

eunsil = "970611-2012345"

print("성별 :", eunsil[7])
print("생년 :", eunsil[0:2]) # 0번째부터 2번째 직전까지
print("생일 :", eunsil[2:6])

print("생년월일 :", eunsil[:6]) # 처음부터 6번쨰 직전까지
print("뒤 7자리 :", eunsil[7:]) # 7번째부터 끝까지

print("뒤에서부터 순차적으로 셀 수 있다 : ", eunsil[-7:])



str_slicing = '안녕하세요. 저는 ***입니다.'

print("첫번째 문자 추출 >> ", str_slicing[0])

print("처음부터:특정위치까지 추출 >> ", str_slicing[:6])  # 0번째는 생략가능
print("특정위치부터:특정위치까지 추출 >> ", str_slicing[10:13])
print("특정위치부터:끝까지 추출 >> ", str_slicing[7:]) 
print("처음부터:끝까지:2칸씩 증가하며 추출 >>", str_slicing[::2])
print("처음부터:끝까지:-1칸씩 감소하며 추출 >>", str_slicing[::-1])
print("양수 사용 >>", str_slicing[7:9])
print("음수 사용 >>", str_slicing[-10:-8])
##############################################################

# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper()) #대문자로 출력
print(python[0].isupper()) #첫번째 문자가 대문자인가?
print(len(python)) #문자열 길이
print(python.replace("Python", "Java")) #문자열의 Python을 찾아 Java로 변환

index = python.index("n") #문자열의 어디에 'n'이 들어있는가
print(index)
index = python.index("n", index + 1)
print(IndexError) #이미 찾은 index뒤에서 부터 다시 찾음

print(python.find("n"))
print(python.find("java")) #원하는 값이 없으면 -1을 return
## print(python.index("Java")) #원하는 값이 없으면 error가 남

print(python.count("n")) # 'n'이 문자열에 몇 번 등장하는가


##############################################################

# 문자열 포맷

print('a' + 'b')
print('a', 'b')

print('나는 %d 살입니다' %20) # %d : 정수
print('나는 %s를 좋아해요' %'파이썬') # %s : 문자열
print('Apple은 %c로 시작해요' %'A') # %c : 문자

# 여러가지를 한꺼번에 출력할 수 있음
print('나는 %s색과 %s색을 좋아해요' %("파란", "빨간")) 

print('나는 {}살입니다.' .format(20))
print('나는 {}색과 {}색을 좋아해요' .format("파란", "빨간"))
print('나는 {0}색과 {1}색을 좋아해요' .format("파란", "빨간"))
print('나는 {1}색과 {0}색을 좋아해요' .format("파란", "빨간")) # 빨간색과 파란색

print('나는 {age}살이며, {color}색을 좋아해요' .format(age = 20, color = "빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

################################################################

# 탈출 문자

# \n : 줄바꿈
print("백문이 불여일견 \n  백견이 불여일타")

print("저는 \"나무코딩\"입니다.")
print("저는 '나무코딩'입니다.")
print('저는 "나무코딩"입니다.')

print("C:\\Users\\Desktop")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 한글자 삭제 (backspace)
print("Redd\b Apple")

# \t : tab
print("Red \t Apple")

##################################################################

# 예제문제

site = input()

index = site.index(".")
pw = site[7:index]

print(str(pw[:3]) + str(len(pw)) + str(pw.count("e")) + "!")

