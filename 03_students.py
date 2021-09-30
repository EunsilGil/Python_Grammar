# 리스트 선언 예시
lst1 = [1, 2, 3, 4, 5]              # 정수형 리스트
lst2 = [0.1, 1.4, 2.99, -1.2]       # 실수형 리스트
lst3 = ["hello", "world", "p", "y"] # 문자열 리스트
# 다양한 자료형을 포함할 수 있다.
lst4 = [1, -0.2, 'hello', True]  

#<------- 문자열과 리스트 -------->
lst_index = [1, 2, 3, 4, 5]
str_index = '12345'

# index를 통한 요소 접근
print(lst_index[1])
print(str_index[1])

# len() 내장 함수 사용
print("예제 리스트의 길이 :", len(lst_index))
print("예제 문자열의 길이 :", len(str_index))

# index를 통한 요소 변경
lst_index[1] = '변경됨'
str_index[1] = '변경됨'   #Error

print(lst_index)
print(str_index)

#<------- 문자열과 리스트 -------->