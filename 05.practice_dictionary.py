cabinet ={
    # key : value
    3 : "유재석",
    100 : "조세호"  
}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# 없는 key를 적어주면 error가 남
# print(cabinet[5])
# 없는 key를 적어도 error가 나지 않음
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))   # key가 5인 값이 있으면 출력, 없으면 이후 str을 출력

# in : key에 해당하는 값이 있는지 없는지 확인
print(3 in cabinet)
print(5 in cabinet)

locker = {
    "A-3" : "유재석",
    "B-100" : "조세호"
}
print(locker)

# update
locker["C-40"] = "김종국"
locker["A-3"] = "김태호"
print(locker)

# delete
del locker["B-100"]
print(locker)

# keys : dictionary의 key들만 출력
print(locker.keys())

# values : dictionary의 value들만 출력
print(locker.values())

# items : key와 value를 pair로 출력
print(locker.items())

# clear : 모든 값 지우기
locker.clear()
print(locker)