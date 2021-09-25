# 집합
# 중복 안됨, 순서 없음
my_set = {1,2,3,4,5}
print(my_set)

set1 = {'유재석', '김태호', '박명수'}
set2 = set(['유재석', '박명수'])

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
set2.add("조세호")
print(set2)

# 삭제
set1.remove("박명수")
print(set1)