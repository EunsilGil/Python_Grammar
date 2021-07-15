# 리스트 : 순서를 가지는 객체 집합

subway =["유재석", "조세호", "박명수"]

#조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하가 다음 정류장에서 탐
subway.append("하하")   #append는 가장 뒤에 추가
print(subway)

#유재석 - 조세호 사이에 정형돈이 탐
subway.insert(1, "정형돈")  #insert(집어넣을 위치, 넣을 것)
print(subway)

#타고 있는 사람들을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 타고 있는가
print(subway.count("유재석"))

# sort: 정렬
num_list = [5, 2, 3, 1, 4]
num_list.sort()
print(num_list)

# reverse: 순서 뒤집기
num_list.reverse()
print(num_list)

# clear : 모두 지우기
num_list.clear()
print(num_list)

# list는 자료형에 구애받지 않고 사용 가능
mix_list = ["eunsil", 25, True]
print(mix_list)

# extend : 두 개의 리스트 확장
subway.extend(mix_list)
print(subway)