# for

for waiting_no in range(5) :
    print('대기번호 : {0}'.format(waiting_no + 1))

for number in range(1, 6):
    print('number : ', number)


starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks :
    print("{0}, 커피가 준비되었습니다.".format(customer))


######################################################
# while

customer = '토르'
index = 5

while index >= 1:
    print('{0}, 커피가 준비되었습니다. {1}번 남았어요'.format(customer, index))
    index -= 1
    if index == 0:
        print('커피는 폐기처분 되었습니다.')

# 무한 루프
# while True : 

customer = '아이언맨'
person = 'Unknown'

while person != customer :
    print('{0}, 커피가 준비되었습니다.'.format(customer))
    person = input('이름이 어떻게 되세요? : ')


#########################################################
# continue and break

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue        # 문장을 더이상 실행시키지 않고 다음 반복으로 넘어감
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break           # 바로 반복문을 종료함
    print("{0}, 책을 읽어봐".format(student))


##########################################################
# 한줄 for

students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]    #ID에 100을 더한 값으로 변경
print(students)

name = ['Iron man', 'Thor', 'Groot']

# len() : 문자열의 길이를 반환 
name = [len(i) for i in name] #학생 이름을 길이로 변환
print(name)

name1 = ['Iron man', 'Thor', 'Groot']

# upper() : 문자열을 모두 대문자로 반환
name1 = [i.upper() for i in name1]
print(name1)


#############################################################
# 예제 문제

# 50명의 승객과 매칭 기회가 있는 택시의 총 탑승객 수 구하기
# 조건1 : 승객별 운행 소요 시간은 5~50분  사이의 난수
# 조건2 : 소요시간 5~15분 사이의 승객만 매칭해야 함

# 출력예제
# [0] 1번쨰 손님 (소요시간 : 15분) 
# [1] 2번째 손님 (소요시간 : 50분)
# [2] 3번째 손님 (소요시간 : 3분)
# ...
# 총 탑승 승객 : 2분

from random import *
count = 0
for 승객 in range(1,51):
    소요시간 = randrange(5, 51)
    
    if 5 <= 소요시간 <=15:
        count += 1
    print('{0}번째 손님 (소요시간 :{1}분)'.format(승객, 소요시간))

print('총 탑승 승객 : {0}명'.format(count))