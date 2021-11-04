# 리스트 선언 예시
lst1 = [1, 2, 3, 4, 5]              # 정수형 리스트
lst2 = [0.1, 1.4, 2.99, -1.2]       # 실수형 리스트
lst3 = ["hello", "world", "p", "y"] # 문자열 리스트
# 다양한 자료형을 포함할 수 있다.
lst4 = [1, -0.2, 'hello', True]  

#<------- 문자열과 리스트 -------->
lst_index = [1, 2, 3, 4, 5]
str_index = '12345'

# 연산자를 활용한 이어쓰기
print(lst_index + ['hello', '리스트'])
print(str_index + "hello문자열")

# index를 통한 요소 접근
print(lst_index[1])
print(str_index[1])

# len() 내장 함수 사용
print("예제 리스트의 길이 :", len(lst_index))
print("예제 문자열의 길이 :", len(str_index))

# index를 통한 요소 변경
lst_index[1] = '변경됨'
# str_index[1] = '변경됨'   #Error

print(lst_index)
print(str_index)

# 값의 복사
mutable1 = [0 , 1, 2, 3]
mutable2 = mutable1     # mutable1의 주소값이 mutable2에 복사됨
mutable2[0] = 5         # 값은 주소값을 참조하고 있으므로 둘 다 값이 변경됨
print(mutable1, mutable2)

immu1 = '12345'
immu2 = immu1   # immu1의 값을 그대로 immu2에 복사
immu2 = '52345' # immu2의 값이 변경된 것이므로 immu1에는 아무런 영향이 X
print(immu1, immu2)

#<------- 리스트 추출하기 -------->
students = ['유재석', '강호동', '신동엽']

# 처음부터 특정 위치까지
print(students[:2])
# 특정위치부터 끝까지
print(students[1:])
# 처음부터 끝까지 2칸씩 
print(students[::2])
# 처음부터 끝까지 -1칸씩 감소 (뒤집기)
print(students[::-1])

#<------- 리스트 처리 함수 -------->
# 주요 리스트 처리 함수 사용 예시
lst = ['p', 'y', 't', 'h', 'o', 'n']

print("예제 리스트의 길이 :", len(lst))
print("예제 리스트의 최댓값 :", max(lst))     # 알파벳 순서에 따라 최댓값 결정
print("예제 리스트의 최솟값 :", min(lst))     # 알파벳 순서에 따라 최솟값 결정

#<------- 리스트 처리 메서드 -------->
# 주요 리스트 처리 메서드 사용 예시
num = [1, 2, 3, 4, 5, 6, 5, 5, 5, 7, 5]

print(num.index(5))   # 5가 가장 처음으로 등장하는 index를 반환
print(num.count(5))

num.append(100)
print(num)            # append는 list의 가장 뒤에 요소를 추가함
num.insert(0, 100)    # insert는 원하는 index에 요소 추가 가능
num.insert(3, 1000)
print(num)            # 기존의 요소는 한 칸씩 뒤로 밀려남

print(num.pop())      # pop할 index 생략시 가장 마지막 요소를 반환 후 삭제
print(num.pop(3))
print(num)

num.remove(5)         # 가장 첫번째로 등장한 5를 삭제
print(num)

num.reverse()         # 현재 리스트를 그래도 reverse
print(num)

num.sort()
print(num)

lst = ['p', 'y', 't', 'h', 'o', 'n']
num.extend(lst)
print(num)

num.clear()
print(num)

#<------- 예제 문제 -------->
# 숫자 10개가 들어 있는 리스트를 입력받아, 그 중 n 번째 요소를 출력하는 프로그램
# 해당 프로그램의 입력은 2가지 입니다.
# 1. 숫자 리스트
# 2. 출력할 index 번호 n
# 출력 : 숫자 리스트에서 n번째 값을 출력합니다.

num_list = [int(input("리스트에 넣을 숫자를 입력하세요 : ")) for _ in range(10)]
n = int(input("몇 번째 요소를 출력할까요? : "))
print(num_list.pop(n-1))