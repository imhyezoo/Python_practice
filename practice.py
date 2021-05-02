#우리집 애완동물 소개
animal = "고양이"
name = "먼지"
age = 4 
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") 
#print(name,"는 ", age, "살이며, ", hobby,"을 아주 좋아해요") -> , 를 쓸 땐 변수에 str X
print(name + "는 어른일까요? " + str(is_adult))


#24:23 퀴즈

station = "사당" #"신도림", "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

#연산자

print(not(1 != 3)) #False

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True #and == &

print((3 > 0) or (3 < 5)) #True
print((3 > 0) | (3 < 5)) #True #or == |

#abs = 절댓값, pow(a,b) = 4^2, max/min(a,b)= a,b중 최댓값/최솟값, round = 반올림

#랜덤함수(난수)

from random import *

print(random()) # 0.0 ~ 1.0중 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10중 임의의 값 생성
print(int(random() * 45 ) + 1) # 1 ~ 45중 임의의 값 생성
print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성

#44:24 quiz 오프라인 스터디 모임 날짜 랜덤으로 정하기
from random import * #난수 사용시 필요한 함수

day = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")
