# list 와 다르게 내용 변경 및 추가 할 수 없고, 속도가 list 보다 빠르다 

menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])

# menu.add('생선까스') # AttributeError: 'tuple' object has no attribute 'add'

# name = '김종국'
# age = 20
# hobby = '코딩'
# print(name, age, hobby)

name, age, hobby = ('김종국', 20, '코딩')
print(name, age, hobby)
