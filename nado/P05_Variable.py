# 애완동물을 소개
animal = '고양이'
name = '해피'
age = 4
hobby = '낮잠'
is_adult = age >=3

print('우리집' + animal + '이름은' + name + '예요')
hobby = '공놀이'
# print(name + '는' +  str(age) +'살이며, ' + hobby + '아주 좋아해요')
# str 정수형을 문자형으로 바꿔줌

print(name, '는',  age,'살이며, ' , hobby , '아주 좋아해요')
# + 대신 ,도 사용가능 대신 띄어쓰기 된다.

print(name + '어른일까요 ?' + str(is_adult))

