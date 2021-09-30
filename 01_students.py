# 변수 선언
int1 = 10
int2 = -10
float1 = 9.9999
float2 = -9.9999
str1 = "python"
str2 = 'hello'
bool1 = int1 >= 3 

#<------- 산술 연산자-------->
print(2 + 3)  # result : 
print(2 - 3)  # result : 
print(2 * 3)  # result : 
print(2 ** 3) # result : 
print(3 / 2)  # result : 
print(4 / 2)  # result : 
print(5 // 3) # result : 
print(5 % 3)  # result : 

# 연산자를 이용해서 문자열의 연산도 가능
# But, 모든 연산이 가능한 것은 아니다.
# 아래 구문들 중 error가 발생하는 식도 있으므로, 추후에 꼭 주석처리를 해줘야한다.
print('hello' * 2)          # result : 
print("l love " + "python") # result :
print("안녕하세요" - "하세요")  # result : 
print("내 수학점수는 " + 0 )   # result : 
print('aaaaaa' / 6)           # result :  

#<------- 비교 연산자-------->
print(10 > 3) # result : 
print(4 >= 7) # result : 
print(10 < 3) # result : 
print(5 <= 5) # result : 
print(3 == 3) # result : 
print(3 == 5) # result : 
print(3 != 3) # result : 
print(3 != 5) # result : 

#<------- 논리 연산자-------->
#and
print((3 > 2) and True)       # result : 
print((3 == 3) and (3 != 3))  # result : 
print((3 != 3) & (4 != 4))    # result : 
# or 
print((3 < 2) or True)        # result : 
print((3 == 3) or (3 != 3))   # result : 
print((3 != 3) | (4 != 4))    # result : 
# not
print(not(3 >= 2))  # result : 
print(not(3 != 3))  # result : 

print (5 > 4 > 3)   # result : 
print (5 > 4 > 7)   # result : 
