# if, elif, else는 연관성이 있는 conditional statement

weather = input('오늘 날씨는 어떤가요? : ')

if weather == '비' or  weather == '눈':
    print('우산을 챙기세요')
elif weather == '미세먼지' :
    print('마스크를 챙기세요')
else :
    print('준비물이 필요 없어요')


temp = int(input("기온은 몇 도 인가요? "))

if temp >= 30 :
    print('너무 더워요. 나가지 마세요')
elif temp >= 10 and temp < 30:
    print('괜찮은 날씨예요!')
elif 0 <= temp < 10:
    print('외투를 챙기세요')
else :
    print('너무 추워요. 나가지 마세요.')