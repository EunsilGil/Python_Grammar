# tuple은 내용 변경과 추가가 불가능 
# 속도가 list보다 빠름
# 변경되지 않는 정보를 저장할 때 편리

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# tuple 활용
(name, age, hobby) = ("김종국", 20, "코딩")
# name, age, hobby = "김종국", 20, "코딩" 로도 나타낼 수 있음
# 변수를 각각 선언하지 않더라도, 변하지 않는 정보에 한해서 tuple로 한번에 관리할 수 있음
print(name, age, hobby)