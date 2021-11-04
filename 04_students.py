#<------- tuple -------->
# tuple 선언 예시
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])

# tuple의 활용
(name, age, hobby) = ("민성", 17, "노래방가기")
print(name)
print(hobby)
print(f"{hobby}살 {name}이는 {hobby}를 좋아합니다.")

#<------- set -------->
# set 선언 예시
my_set = {1,2,3,4,5}
print(my_set)

set1 = {'원슈타인', '이지아', '머쉬베놈', '정준하'}
set2 = set(['원슈타인', '머쉬베놈', '개코'])    # list를 set으로 형변환

# 교집합
print(set1 & set2)
print(set1.intersection(set2))

# 합집합
print(set1 | set2)
print(set1.union(set2))

# 차집합
print(set1 - set2)
print(set1.difference(set2))

# 추가
set2.add("지코")
print(set2)

# 삭제
set1.remove("이지아")
print(set1)

#<------- dict -------->
# dict 선언 예시
cabinet ={
    # key : value
    3 : "유재석",
    100 : "조세호"  
}
print(cabinet[3])
print(cabinet[100])
print(cabinet[5]) 

# in : key에 해당하는 값이 있는지 없는지 확인
print(3 in cabinet)
print(5 in cabinet)

locker = {
    'A-2' : '엄마상어',
    'B-100' : '아빠상어',
    'C-7' : '할머니상어'
}
print(locker)

# update
locker["C-40"] = "할아버지상어"
locker["A-2"] = "아기상어"
print(locker)

# delete
del locker["B-100"]
print(locker)

# dict 관련 메서드
address = {
    '히밥' : '010-0000-7979',
    '입짧은햇님' : '010-0691-0691',
    '탁주TV' : '010-1234-1234'
}

print(address.get('캐리TV'))
print(address.get('캐리TV', '번호 없음'))

print(address.keys())

print(address.values())

print(address.items())

print(address.clear())

#<------- 자료형변환-------->
menu = {"커피", "우유", "주스"} # set
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))